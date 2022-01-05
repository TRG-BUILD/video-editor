from typing import List, Any
from os.path import isfile, isdir

from classes.scene import Scene
from classes.transition import Transition
from classes.video import Video

def edit():
    """edit is the main function, receiving input from the user, to manipulate the Video object"""

    print("This editor creates a single video, following three steps")
    print("First, any amount of footage will be loaded into a Video object")
    print("Second, the Video objects footage can then be edited")
    print("Third, the Video will concatenate all the footage into a single video, and save to the chosen location")

    print("\nLoad footage\n")
    video = load_video_view()
    print("\nEdit footage\n")
    video = edit_video_view(video)
    print("\nPublish video\n")
    publish_video_view(video)

    return True
    

def load_video_view():
    load_more_videos = True
    video = Video()
    print("Give the path to a video for editing, or enter STOP if you have already loaded all videos in for editing")
    print("Give the absolute path to your video, for instance:")
    print("C:\\path\\to\\your\\video.mov")
    loaded_videos = 0
    while load_more_videos:
        command = input("Please enter in a new path or STOP\n")
        command = _validate_command(command)
        if not command:
            print("You entered in a non-valid command, try again\n")
        elif command == "STOP":
            load_more_videos = False
        else:
            loaded_videos += 1
            video.add_video(command)
            print("You now edit (", loaded_videos, ") videos!")

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
    while command != "0":
        if command == "1":
            pass
        elif command == "2":
            pass
        elif command == "3":
            pass
        elif command == "4":
            pass
        else:
            print("Invalid command, try again")

    print("Exiting the editing phase")
    return video

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
    #edit()

    """
        Timestamps:
        0:03    Introduktion
        0:52    Introduktion-prints og kommentarer
        1:57    Introduktion-overblik af filer
        2:45    Datatyper
        3:45    Datatyper-strenge
        8:43    Datatyper-tal
        11:49   Datatyper-bools
        13:56   Datastrukturer
        14:21   Datastrukturer-variable
        18:49   Datastrukturer-lister
        24:48   Datastrukturer-dictionaries
        28:58   Kontrolstrukturer
        29:17   Kontrolstrukturer-conditions
        32:23   Kontrolstrukturer-for loop
        39:20   Kontrolstrukturer-while loop
        41:55   Kontrolstrukturer-funktioner
        46:33   Brugbare funktioner
        49:22   lidt om "lazy" funktioner
        50:55   Exceptions
        51:47   Exceptions-Syntax og Name Error
        54:23   Exceptions-try catch og Type Error
        56:31   Exceptions-Attribute Error
        57:46   Exceptions-Value Error
        59:57   Libraries
        1:01:18 Importing Libraries
        1:03:23 StandardLibrary-Statistics
        1:04:40 Pandas
        1:24:41 Matplotlib
        1:27:06 FEJL! Plottet bliver desværre ikke vist i video optagelsen! Prøv at kør filen selv og følg med :)
        1:35:10 Psycopg2
        1:56:49 Det vigtigste

    """
    import ffmpeg
    path = "C:\\Users\\Martin\\Pictures\\Camera Roll\\Videos"
    file1 = ffmpeg.input(path + "\\SamletOversigtsVideo1.mkv")
    v1 = file1.video
    #v1 = v1.filter("trim",start=5349).setpts("PTS-STARTPTS")
    a1 = file1.audio
    #a1 = a1.filter("atrim",start=5349).filter("asetpts", "PTS-STARTPTS")
    file2 = ffmpeg.input(path + "\\SamletOversigtsVideo2.mkv")
    v2 = file2.video
    #v2 = v2.filter("trim", start=10, duration=30)
    a2 = file2.audio
    #a2 = a2.filter("atrim",start=10, duration=30)
    #file3 = ffmpeg.input(path + "\\Done3.mkv")
    #v3 = file3.video
    #a3 = file3.audio
    #file4 = ffmpeg.input(path + "\\Done4.mkv")
    #v4 = file4.video
    #a4 = file4.audio
    #file5 = ffmpeg.input(path + "\\Done5.mkv")
    #v5 = file5.video
    #a5 = file5.audio

    #joined = ffmpeg.concat(v1,a1,v2,a2,v3,a3,v4,a4,v5,a5,v=1,a=1).node
    joined = ffmpeg.concat(v1,a1,v2,a2,v=1,a=1).node
    v6 = joined[0]
    a6 = joined[1].filter('volume', 0.9)
    out = ffmpeg.output(v6, a6, path + '\\SamletOversigtsVideo.mkv')
    out.run()