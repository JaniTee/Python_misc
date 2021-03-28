#!python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# AVATAAN SELAIMELLA SIVUSTO 2048 peliin, ja painetan ylös, oikealle, alas ja vasemmalle näppäimiä.
# Tehdään tämä 5 kertaa, kirjataan tulokset logiin ylös.

print('TULOKSET/SCORES:')
for j in range(15):      #HOW MANY TIMES GAME IS PLAYED, NOW 15
    browser = webdriver.Chrome()
    browser.get('https://gabrielecirulli.github.io/2048/')
    #browser.maximize_window()         # OPEN BROWSER IN FULL-SCREEN
    html = browser.find_element_by_tag_name('html')
    for i in range(200):
        # RIGHT,UP,DOWN,LEFT KEYS ARE PRESSED IN BROWSER 200 TIMES.
        html.send_keys(Keys.RIGHT)
        #time.sleep(0.2)
        html.send_keys(Keys.UP)
        #time.sleep(0.2)
        html.send_keys(Keys.DOWN)
        #time.sleep(0.2)
        html.send_keys(Keys.LEFT)
        #time.sleep(0.2)
    score = browser.find_element_by_css_selector("div[class='score-container']")    #HAETAAN TULOS JA TULOSTETAAN SE
    print(score.text)       #PISTEIDEN TULOSTUS
    # TEHDÄÄN .txt TIEDOSTOON LOGI TULOKSISTA, JOS HALUAA JÄTTÄÄ VAIKKA YÖKSI PÄÄLLE BOTIN JYRÄÄMÄÄN(OLETUKSENA WORKING DIRECTORY).
    if(i == 0):
        scoreFile = open('scores.txt', 'w')
        scoreFile.write('Results of the game:\n' + score.text + '\n')
        scoreFile.close()
    else:
        scoreFile = open('scores.txt', 'a')
        scoreFile.write(score.text + '\n')
        scoreFile.close()
    browser.quit()

browser.quit()