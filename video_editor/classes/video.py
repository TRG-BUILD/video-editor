import ffmpeg
from .scene import Scene

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
        self.footage.append(Scene(path))

    def save_video(self, output_path):
        for scene in self.footage:
            if self.stream:
                self.stream = ffmpeg.concat(self.stream, scene.stream)
            else:
                self.stream = ffmpeg.input(scene.stream)
        stream = ffmpeg.output(self.stream, output_path)
        ffmpeg.run(stream)
        