import ctypes
import time
import psutil
from datetime import datetime

# Constants
VOLUME_INCREMENT = 5
VOLUME_DECREMENT = 5
INACTIVE_THRESHOLD = 300  # 5 minutes

# Function to get the current volume
def get_current_volume():
    mixer = ctypes.windll.winmm.waveOutGetVolume
    # Get the current volume level
    volume = ctypes.c_uint()
    mixer(0, ctypes.byref(volume))
    current_volume = volume.value & 0xffff
    return current_volume

# Function to set the system volume
def set_volume(volume):
    mixer = ctypes.windll.winmm.waveOutSetVolume
    # Set the volume level
    volume = max(0, min(65535, volume))
    mixer(0, volume | (volume << 16))

# Function to check if the user is active
def is_user_active():
    idle_time = psutil.boot_time() - psutil.cpu_times().idle
    return idle_time < INACTIVE_THRESHOLD

# Function to adjust volume based on user activity
def adjust_volume():
    current_volume = get_current_volume()
    if is_user_active():
        # Increase volume if user is active
        new_volume = current_volume + VOLUME_INCREMENT
    else:
        # Decrease volume if user is inactive
        new_volume = current_volume - VOLUME_DECREMENT
    set_volume(new_volume)

# Main function to run the TechDash program
def main():
    print("TechDash is running...")
    try:
        while True:
            adjust_volume()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print("TechDash stopped.")

if __name__ == "__main__":
    main()