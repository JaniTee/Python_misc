#!python3

# Haetaan tällä ohjelmalla 5 ensimmäistä pypi.org sivuston projektihakua(terminaaliargumentin mukaan). 
# Toimii seuraavasti: python3 searchpypi.py "hakusanasi"

import requests, sys, webbrowser, bs4

print('Searching...') # Näytetään tämä kun haetaan tietoja.
res2 = requests.get('https://pypi.org/search?q=' + ' '.join(sys.argv[1:]))

soup = bs4.BeautifulSoup(res2.text,'html.parser')

elementit = soup.select('.package-snippet') # package-snippet css selector löytyy jokaisesta haun linkistä.

# Avataan viisi ensimmäistä hakutulosta.
for i in range(len(elementit)):
        if(i < 5):
            print('Avataan..:' + 'https://pypi.org' + elementit[i].get('href'))
            webbrowser.open('https://pypi.org/' + elementit[i].get('href'))
