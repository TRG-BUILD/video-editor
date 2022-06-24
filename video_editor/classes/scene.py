import ffmpeg

class Scene:
    """A single scene which is the footage being shown"""

    def __init__(self, path, has_sound):
        self.path = path
        self.name = path.split("\\")[-1]
        self.stream = ffmpeg.input(path)
        self.video = self.stream.video
        self.audio = self.stream.audio
        self.has_sound = has_sound
        
    def __str__(self):
        return self.name