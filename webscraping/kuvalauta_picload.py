#!python3

# Pic loader - ladataan annetun langan kaikki kuvat koneelle.

import os, requests, bs4, time
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}

print('Syötä langan osoite jonka kuvat haluat ladata koneellesi:')
url = input()
kansion_nimi = 'Kuvalaudat' + url[27:]
os.makedirs(kansion_nimi, exist_ok=True)  #Tehdään Langan_kuvat niminen kansio siihen kansioon jossa skripti ajetaan.

#Ladatan sivusto
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')   
#print(soup)

#Haetaan kuvaelementit/videoiden linkit taulukkoon, ja ladataan ne kansioon "Langan_kuvat"
kuvaElementit = soup.select('.fileThumb')
startTime = time.time()
for i in range(len(kuvaElementit)):
    kuvaURL = 'https:' + kuvaElementit[i].get('href')

    #Ladataan kuva
    print('Downloading image %s...' % (kuvaURL))
    res = requests.get(kuvaURL)
    res.raise_for_status()

    #Tallennetaan se koneelle
    mediaFile = open(os.path.join(kansion_nimi, os.path.basename(kuvaURL)), 'wb')
    for chunk in res.iter_content(100000000):
        mediaFile.write(chunk)
    mediaFile.close()
endTime = time.time()
timeExpired = (endTime - startTime)
timeExpired = round(timeExpired, 2)
print('Langan kuvat ladattu. Löytyy Kuvalaudat: kansion alta. Latauksessa kesti %s sekuntia. Suljetaan ohjelma.' % (timeExpired))
