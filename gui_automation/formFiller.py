#!python3

# formFiller.py - Fills this form: https://autbor.com/form , depending data on the formData table

import pyautogui, time, webbrowser


formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
            {'name': 'Jani Tiainen', 'fear': 'Spiders', 'source': 'crystal ball',
            'robocop': 3, 'comments': 'Sen minka voi jattaa tekematta tanaan, voi myos huomenna.'},
           ]


for i in range(len(formData)):
    time.sleep(0.5)   
    if i == 0:
        webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform')
    time.sleep(1.5)
    pyautogui.write('\t',interval=0.15)
    pyautogui.write('\t',interval=0.15)
    pyautogui.write(formData[i]['name'],interval=0.05)
    pyautogui.write('\t')
    time.sleep(0.25)
    pyautogui.write(formData[i]['fear'],interval=0.05)
    pyautogui.write('\t')
    time.sleep(0.25)

    if formData[i]['source'] == 'wand':
        pyautogui.press('down',interval=0.25)
        pyautogui.write('\n',interval=0.25)
        pyautogui.write('\t',interval=0.25)
    elif formData[i]['source'] == 'amulet':
        pyautogui.press('down',interval=0.25)
        pyautogui.press('down',interval=0.25)
        pyautogui.write('\n',interval=0.25)
        pyautogui.write('\t',interval=0.25)
    elif formData[i]['source'] == 'crystal ball':
        pyautogui.press('down',interval=0.25)
        pyautogui.press('down',interval=0.25)
        pyautogui.press('down',interval=0.25)
        pyautogui.write('\n',interval=0.25)
        pyautogui.write('\t',interval=0.25)
    elif formData[i]['source'] == 'money':
        pyautogui.press('down',interval=0.25)
        pyautogui.press('down',interval=0.25)
        pyautogui.press('down',interval=0.25)
        pyautogui.press('down',interval=0.25)
        pyautogui.write('\n',interval=0.25)
        pyautogui.write('\t',interval=0.25)

    time.sleep(1)
    pyautogui.write('\t',interval=0.25)

    robo = 1
    if formData[i]['robocop'] == 1:
        pyautogui.press('right',interval=0.25)
        pyautogui.press('left')
    else:
        while robo < (formData[i]['robocop']):
            pyautogui.press('right',interval=0.25)
            robo = robo + 1
    pyautogui.write('\t\t')

    time.sleep(1)
    pyautogui.write(formData[i]['comments'],interval=0.05)
    pyautogui.write('\t\n')
    time.sleep(1)
    pyautogui.write('\t\n')
