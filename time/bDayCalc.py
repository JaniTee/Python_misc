#! python3
# bDayCalc - Calculates how long is till my bday!

import time, datetime, subprocess

bday = datetime.datetime(yyyy,d,m,0,0,0)
while(datetime.datetime.now() < bday):
    timeLeft = bday - datetime.datetime.now()
    print('Syntymäpäivääni on aikaa: ' + str(timeLeft), end='\r')
    time.sleep(1)

subprocess.Popen(['open', '/Users/janitiainen/Documents/sound.wav'])
