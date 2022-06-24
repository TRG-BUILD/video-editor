from typing import List, Any
from os.path import isfile, isdir

from classes.scene import Scene
from classes.video import Video

def edit():
    """edit is the main function, receiving input from the user, to manipulate the Video object"""

    print("This editor creates a single video, following three steps")
    print("First, load one video to edit it, or multiple videos to add them together")
    print("Second, if you have only one video, it can now be edited")
    print("Third, the program will create the new video at the location you choose")

    print("\nLoad footage\n")
    video = load_video_view()
    print("\nEdit footage\n")
    video = edit_video_view(video)
    print("\nPublish video\n")
    publish_video_view(video)

    return True
    

def load_video_view():
    video = Video()
    print("Give the path to a video for editing. You can only edit one video at a time.")
    print("Give the absolute path to your video, for instance:")
    print("C:\\path\\to\\your\\video.mov")
    try_again = True
    while try_again:
        path = input("Please enter in a new path or STOP\n")
        path = _validate_command(path)
        if not path:
            print("You entered in a non-valid path, try again\n")
        else:
            while try_again:
                has_sound = input("Does the video have sound? Write 'y' or 'n'")
                has_sound = True if has_sound == "y" else False if has_sound == "n" else None
                if has_sound is not None:
                    video.add_video(path, has_sound)
                    try_again = False
                else:
                    print("Please write lower case y or n only. Just a single letter")

    return video


def _validate_command(command):
    if(command == "STOP"):
        return "STOP"
    elif isfile(command):
        return command
    else:
        return False

def edit_video_view(video):
    print("\n\n")
    print("To choose a command, write its corresponding number")
    print("All scenes will be automatically concatenated at the end")
    print("Supported commands as of this moment is")
    print("0: Exit, and go to the publishing phase")
    print("1: Information, regarding the current state of the video")
    print("2: Cut, a video, by choosing the segment you want")
    command = "start"
    while command != "0":
        command = input("Please enter your command (a single digit)")
        print("\n\n\n")
        if command == "0":
            print("Exiting the editing phase")
        elif command == "1":
            print("The video: " + str(video))
            print("Currently contains the following cuts")
            for cut in video.cuts:
                print(str(cut))
        elif command == "2":
            try_again = True
            while try_again:
                start_time = input("Please enter the starttime of the cut (in HH:MM:SS format)\n")
                end_time = input("Please enter the endtime of the cut (in HH:MM:SS format)\n")
                if _valid_time(start_time) and _valid_time(end_time):
                    if(video.add_cut(start_time, end_time)):
                        print("The following cut has been registered successfully")
                        print(str(video.cuts[-1]))
                    else:
                        print("The cut was not valid. Did you check that start_time is lower than end_time and the video is that long?")
                    try_again = False
                else:
                    print("Starttime or Endtime does not follow the correct format (HH:MM:SS)")
                    print("An example might be '00:04:23' for 4 minutes and 23 seconds into the video")
                    print("Try again")
        else:
            print("Invalid command, try again")

    return video

def _valid_time(time):
    try:
        int(time[0])
        int(time[1])
        time[2] == ":"
        int(time[3])
        int(time[4])
        time[5] == ":"
        int(time[6])
        int(time[7])
        return True
    except Exception as e:
        return False

def publish_video_view(video):
    path = input("Please enter the path to the directory you want the file to be created at.\n")
    if isdir(path):
        name = input("please enter the name of your file, remember extension type\n")
        location = path + "\\" + name
        video.save_video(location)
        print("\nVideo published at ", location, "\n")
    else:
        print("You entered in a non-valid path, try again\n")
        publish_video_view(video)

if __name__ == '__main__':
    edit()