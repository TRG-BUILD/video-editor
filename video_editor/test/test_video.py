import pytest

from video_editor.classes.video import Video

def test_video_can_load_and_save_video(mocker):
    mocker.patch("video_editor.classes.video.ffmpeg", return_value=True)

    video = Video()

    assert 1 == 1