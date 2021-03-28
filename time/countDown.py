#! python3
# countdown.py - Countdown and play a sound at the end.

import time, subprocess

timeLeft = 5
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['open', 'path_to_file_here'])
