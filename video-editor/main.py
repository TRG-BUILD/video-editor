from typing import List, Any
from os.path import isfile, isdir

from classes.scene import Scene
from classes.transition import Transition
from classes.video import Video

def edit():
    """edit is the main function, receiving input from the user, to manipulate the Video object"""

    print("This editor creates a single video, following three steps")
    print("First, any amount of footage will be loaded into a Video object")
    print("Second, the Video object will be edited to consist of 1 to more scenes and/or transitions")
    print("Third, the Video will be published to a chosen location")

    video = load_video_view()
    video = edit_video_view(video)
    publish_video_view(video)

    return True
    

def load_video_view():
    print("LOAD")
    load_more_videos = True
    video = Video()
    while load_more_videos:
        print("Give the path to a video for editing, or enter STOP if you have already loaded all videos in for editing")
        print("Give the absolute path to your video, for instance:")
        print("C:/path/to/your/video.mov")
        command = input("Please enter in your path or STOP\n")
        command = _validate_command(command)
        if not command:
            print("You entered in a non-valid command, try again\n")
        elif command == "STOP":
            load_more_videos = False
        else:
            video.add_video(command)
            print("LOAD SUCCESFULL\n")

    return video


def _validate_command(command):
    if(command == "STOP"):
        return "STOP"
    elif isfile(command):
        return command
    else:
        return False

def edit_video_view(video):
    print("EDIT")
    video.start_edit()

    print("Editing has begun")

    return video

def publish_video_view(video):
    print("PUBLISH")
    path = input("Please enter the path to the directory you want the file to be created at.\n")
    if isdir(path):
        name = input("please enter the name of your file, remember extension type\n")
        video.save_video(path + "\\" + name)
    else:
        print("You entered in a non-valid path, try again\n")
        publish_video_view(video)

if __name__ == '__main__':
    edit()