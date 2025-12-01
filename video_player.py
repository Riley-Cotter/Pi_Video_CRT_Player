import os
import vlc
import time

VIDEO_DIR = "/media/usb"
VIDEO_EXT = (".mp4", ".mkv", ".avi", ".mov")

# create VLC instance with no video window decorations / fullscreen (if supported)
instance = vlc.Instance("--fullscreen", "--no-video-deco", "--no-embedded-video")

while True:
    files = sorted([
        os.path.join(VIDEO_DIR, f)
        for f in os.listdir(VIDEO_DIR)
        if f.lower().endswith(VIDEO_EXT)
    ])

    for video in files:
        print("Playing:", video)
        player = instance.media_player_new()
        media = instance.media_new(video)
        player.set_media(media)
        player.play()
        # wait until video finishes
        # approximate method: poll for state
        while True:
            state = player.get_state()
            # Ended = 6, Error = 3, Stopped = 5
            if state in (vlc.State.Ended, vlc.State.Error, vlc.State.Stopped):
                break
            time.sleep(0.5)
        time.sleep(1)
