#! python3
# mapIt.py - Lauches a map in the browser using an adress from the command line argument, or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #Get address from command line
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

