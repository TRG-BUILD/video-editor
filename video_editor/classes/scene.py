import ffmpeg

class Scene:
    """A single scene which is the footage being shown"""

    def __init__(self, path):
        self.path = path
        self.name = path.split("\\")[-1]
        stream = ffmpeg.input(path)
        self.video = stream.video
        self.audio = stream.audio
