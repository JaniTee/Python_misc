#!python3
# twitterpostin.py - Ask user their login information, and post they want to post, and post it to twitter.

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

# KYSYTÄÄN KÄYTTÄJÄLTÄ SALASANA, PASSU JA MITÄ HALUAA POSTATA. LAITETAAN NÄMÄ MUUTTUJIIN TALTEEN.
print('Tell me your Twitter login email:')
email = input()
print('Tell me your Twitter password')
passw = input()
print('What do you want to post?')
tw_post = input()

# AVATAAN TWITTERIN SIVUSTO
browser = webdriver.Chrome()
browser.get('https://twitter.com')

# HELPOIN TAPA VALITA TIETTY CS SELECTOR ON: browser.find_element_by_css_selector("div[class='Classin nimi, tai mikä selector onkaan']")

time.sleep(1)

# LOGIN BUTTON CSS SELECTOR JA KLIKATAAN NAPPIA
loginButton = browser.find_element_by_css_selector("div[class='css-901oao r-1awozwy r-13gxpu9 r-6koalj r-18u37iz r-16y2uox r-1qd0xha r-a023e6 r-b88u0q r-1777fci r-ad9z0x r-dnmrzs r-bcqeeo r-q4m81j r-qvutc0']")
loginButton.click()
time.sleep(1)       # MUISTETAAN AINA LAITTAA PIENI TAUKO ETTÄ SIVUSTO KERKEÄÄ LADATA

# EMAIL CSS SELECTOR JA INPUT
emailID = browser.find_element_by_css_selector("input[class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")
emailID.send_keys(email)
time.sleep(1)       

# SALASANA CSS SELECTOR JA INPUT
passID = browser.find_element_by_css_selector("input[name='session[password]']")
passID.send_keys(passw)                                                
passID.submit()
time.sleep(5)       # TÄSSÄ HIEMAN PIDEMPI TAUKO, KUN LADATAAN SIVUSTO

# SYÖTETÄÄN POSTAUS KENTTÄÄN POSTAUS
postaus = browser.find_element_by_css_selector("div[class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
postaus.send_keys(tw_post)
time.sleep(1)

# ETSITÄÄN ‘TWEET’ NAPPULA JA PAINETAAN SITÄ
tweetButton = browser.find_element_by_css_selector("div[class='css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-1n0xq6e r-1vuscfd r-1dhvaqw r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr']")
tweetButton.click()
time.sleep(5)

# SULJETAAN SELAIN JA LOPETETAAN OHJELMA
browser.quit()