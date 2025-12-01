#!/usr/bin/env python3
"""
Video Looper for Raspberry Pi
Plays all videos from /media/usb in a continuous loop using VLC
"""

import os
import subprocess
import time
from pathlib import Path

# Configuration
VIDEO_DIR = "/media/usb"
VIDEO_EXTENSIONS = {'.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.m4v', '.mpg', '.mpeg'}

def find_videos(directory):
    """
    Recursively find all video files in the specified directory
    Returns a sorted list of video file paths
    """
    videos = []
    
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if Path(file).suffix.lower() in VIDEO_EXTENSIONS:
                    full_path = os.path.join(root, file)
                    videos.append(full_path)
    except Exception as e:
        print(f"Error scanning directory: {e}")
        return []
    
    # Sort alphabetically for consistent playback order
    videos.sort()
    return videos

def play_video(video_path):
    """
    Play a single video using VLC in fullscreen mode
    Returns True if video played successfully, False otherwise
    """
    try:
        print(f"Playing: {video_path}")

        # Set up environment variables for VLC
        env = os.environ.copy()
        
        # Create runtime directory if it doesn't exist
        runtime_dir = f"/run/user/{os.getuid()}"
        if not os.path.exists(runtime_dir):
            try:
                os.makedirs(runtime_dir, mode=0o700, exist_ok=True)
            except:
                runtime_dir = "/tmp"
        
        env['XDG_RUNTIME_DIR'] = runtime_dir
        env['HOME'] = os.path.expanduser('~')
        
        # VLC command with fullscreen and quit after playback
        subprocess.run([
            'cvlc',
            '--fullscreen',
            '--play-and-exit',
            '--no-video-title-show',
            '--no-osd',
            '--vout=fb',
            '--fbdev=/dev/fb0',
            '--aout=alsa',
            '--no-xlib',
            '--no-dbus',
     
            video_path
        ], check=True)
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error playing video: {e}")
        return False

def main():
    """
    Main loop: index videos and play them continuously
    """
    print("Video Looper Starting...")
    print(f"Scanning directory: {VIDEO_DIR}")
    
    # Check if directory exists
    if not os.path.exists(VIDEO_DIR):
        print(f"Error: Directory {VIDEO_DIR} does not exist!")
        return
    
    while True:
        # Index videos (re-scan each loop in case USB content changes)
        videos = find_videos(VIDEO_DIR)
        
        if not videos:
            print(f"No videos found in {VIDEO_DIR}")
            print("Waiting 10 seconds before retrying...")
            time.sleep(10)
            continue
        
        print(f"Found {len(videos)} video(s)")
        print("-" * 50)
        
        # Play each video
        for video in videos:
            play_video(video)
            time.sleep(1)  # Brief pause between videos
        
        print("\nCompleted playlist. Restarting loop...")
        print("-" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nVideo looper stopped by user")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
