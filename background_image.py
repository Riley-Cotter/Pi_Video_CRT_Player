import glob
import subprocess
import logging
import time
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def wait_for_usb_mount(mount_path="/media/usb", timeout=30):
    start_time = time.time()
    logging.info(f"Waiting for USB mount at {mount_path}...")

    while time.time() - start_time < timeout:
        try:
            with open("/proc/mounts", "r") as mounts:
                if any(mount_path in line for line in mounts):
                    logging.info("USB is mounted.")
                    return True
        except Exception as e:
            logging.error(f"Error checking mounts: {e}")

        time.sleep(1)

    logging.error(f"ERROR: USB not mounted after {timeout} seconds.")
    return False


if __name__ == "__main__":
    if not wait_for_usb_mount():
        logging.error("USB mount failed, aborting image display.")
        exit(1)

    jpg_files = glob.glob("/media/usb/*.jpg")

    if not jpg_files:
        logging.warning("No JPG images found in /media/usb/. Skipping image display.")
        exit(0)

    # Prefer fbi if framebuffer exists
    if os.path.exists("/dev/fb0"):
        cmd = ["sudo", "fbi", "-T", "2", "-a", "--noverbose", "-noreset"] + jpg_files
        viewer = "fbi"
    else:
        cmd = ["feh", "-F", "-Z"] + jpg_files
        viewer = "feh"

    try:
        logging.info(f"Using {viewer} to display images.")
        subprocess.run(cmd, check=True)
        logging.info("Displayed image(s) successfully.")
    except Exception as e:
        logging.error(f"Error running {viewer}: {e}")
