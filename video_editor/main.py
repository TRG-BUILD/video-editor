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

    print("Load footage")
    video = load_video_view()
    print("Edit footage")
    video = edit_video_view(video)
    print("Publish video")
    publish_video_view(video)
    print("Video published")

    return True
    

def load_video_view():
    load_more_videos = True
    video = Video()
    print("Give the path to a video for editing, or enter STOP if you have already loaded all videos in for editing")
    print("Give the absolute path to your video, for instance:")
    print("C:/path/to/your/video.mov")
    while load_more_videos:    
        command = input("Please enter in a new path or STOP\n")
        command = _validate_command(command)
        if not command:
            print("You entered in a non-valid command, try again\n")
        elif command == "STOP":
            load_more_videos = False
        else:
            video.add_video(command)
            print("LOAD SUCCESFULL\n")

    video.start_edit()
    return video


def _validate_command(command):
    if(command == "STOP"):
        return "STOP"
    elif isfile(command):
        return command
    else:
        return False

def edit_video_view(video):
    print("To choose a command, write its corresponding number")
    print("All scenes will be automatically concatenated at the end")
    print("Supported commands as of this moment is")
    print("0: Exit, and go to the publishing phase")
    print("1: Information, regarding the current state of the video")
    print("2: Cut, a video to split a scene into two scenes")
    print("3: Remove, a scene from the video")
    print("4: Move, a scene around in its internal ordering")

    command = input("Please enter your command (a single digit)")
    if command == "0":
        print("Exiting the editing phase")
        return video
    elif command == "1":
        pass
    elif command == "2":
        pass
    elif command == "3":
        pass
    elif command == "4":
        pass
    else:
        print("Invalid command, try again")
    
    edit_video_view(video)

    

def publish_video_view(video):
    path = input("Please enter the path to the directory you want the file to be created at.\n")
    if isdir(path):
        name = input("please enter the name of your file, remember extension type\n")
        video.save_video(path + "\\" + name)
    else:
        print("You entered in a non-valid path, try again\n")
        publish_video_view(video)

if __name__ == '__main__':
    edit()