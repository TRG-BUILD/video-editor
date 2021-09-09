import ffmpeg

class Video:
    """A Video is the class being constituted by Scenes and Transitions, as well as any needed metadata"""

    def __init__(self):
        self.stream = None
        self.footage = []

    def __str__(self):
        name = "Video containing footage from:\n"
        for video in self.footage:
            name += video["name"] + "\n"
        return name

    def add_video(self, path):
        self.footage.append({"name": path.split("\\")[-1], "path": path})

    def start_edit(self):
        main_stream = None
        for video in self.footage:
            if main_stream:
                streams = [main_stream]
                streams.append(ffmpeg.input(video["path"]))
                main_stream = ffmpeg.concat(streams)
            else:
                main_stream = ffmpeg.input(video["path"])
        
        self.stream = main_stream

    def save_video(self, path):
        stream = ffmpeg.output(self.stream, path)
        ffmpeg.run(stream)
        