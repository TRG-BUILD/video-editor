import ffmpeg
from .scene import Scene

class Video:
    """A Video is the class being constituted by Scenes and Transitions, as well as any needed metadata"""

    def __init__(self):
        self.video = None
        self.has_sound = False
        self.cuts = []

    def __str__(self):
        return "Edit of " + self.video.name

    def add_video(self, path, has_sound):
        self.video = Scene(path, has_sound)
        self.has_sound = has_sound
        
    def add_cut(self, start_time, end_time):
        start_sec = self._convert_time_to_seconds(start_time)
        end_sec = self._convert_time_to_seconds(end_time)
        new_cut = Scene(self.video.path, self.video.has_sound)
        new_cut.name = "Cut from " + start_time + " to " + end_time
        new_cut.video = new_cut.stream.video.filter("trim",start=start_sec, end=end_sec).setpts("PTS-STARTPTS")
        new_cut.audio = new_cut.stream.audio.filter("atrim",start=start_sec, end=end_sec).filter("asetpts", "PTS-STARTPTS")
        self.cuts.append(new_cut)
        return True
    
    def _convert_time_to_seconds(self, time):
        SEC_PR_HOUR = 3600
        SEC_PR_MIN = 60
        seconds = 0
        # It follows: 00:00:00 format
        seconds += int(time[0] * 10 * SEC_PR_HOUR)
        seconds += int(time[1] * SEC_PR_HOUR)
        seconds += int(time[3] * 10 * SEC_PR_MIN)
        seconds += int(time[4] * SEC_PR_MIN)
        seconds += int(time[6] * 10)
        seconds += int(time[7])
        
        return seconds

    def save_video(self, output_path):
        if len(self.cuts) == 0:
            file1 = self.video.stream
            out = ffmpeg.output(file1, output_path)
            out.run()
            return True
            
        stream_list = []
        for scene in self.cuts:
            stream_list.append(scene.video)
            if self.has_sound:
                stream_list.append(scene.audio)
            
        if self.has_sound:
            joined = ffmpeg.concat(*stream_list, v=1, a=1).node
            video_stream = joined[0]
            audio_stream = joined[1]
            out = ffmpeg.output(video_stream, audio_stream, output_path)
        else:
            joined = ffmpeg.concat(*stream_list, v=1, a=0).node
            video_stream = joined[0]
            out = ffmpeg.output(video_stream, output_path)
        out.run()
        return True