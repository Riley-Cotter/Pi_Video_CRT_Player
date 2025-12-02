import os
import vlc
import time

VIDEO_DIR = "/media/usb"
VIDEO_EXT = (".mp4", ".mkv", ".avi", ".mov")

# VLC instance for framebuffer (no X)
instance = vlc.Instance("--autoscale")

while True:
    files = sorted([
        os.path.join(VIDEO_DIR, f)
        for f in os.listdir(VIDEO_DIR)
        if f.lower().endswith(VIDEO_EXT)
    ])

    for video in files:
        player = instance.media_player_new()
        media = instance.media_new(video)
        player.set_media(media)

        # Set the aspect ratio (e.g., "16:9" for widescreen)
        player.video_set_aspect_ratio("4:3")
        
        player.play()
        while True:
            state = player.get_state()
            if state in (vlc.State.Ended, vlc.State.Error, vlc.State.Stopped):
                break
            time.sleep(0.5)
        time.sleep(1)
