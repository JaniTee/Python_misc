#! python3
# toriKitaraLataaja - ladataan torin myynnissä olevien kitaroiden kuvat, voit määritellä määrän uusimmasta ilmoitukseta taaksepäin.

import os, requests, bs4, time, datetime, pyinputplus as pyip

print('Montako sivua kuvia haluat ladata?')
sivuMaara = pyip.inputNum()

for i in range(sivuMaara):
    #Kun offset on 0, ollaan aina ensimmäisellä sivulla. 15 on toinen sivu, 30 kolmas jne. Nousee aina 15 per sivu.
    offset = 0

    if(i > 0):
        offset = i * 15
    
    url = 'https://muusikoiden.net/tori/?category=8&offset=%s' % str(offset)
    timestamp = datetime.datetime.now().strftime('%d_%m_%H_%M')

    # Luodaan kitaroiden_kuvat niminen kansio aikastampilla.
    if(i < 1):
        kansio = 'kitaroidenKuvat_' + str(timestamp)
        os.makedirs(kansio, exist_ok=True)

    res = requests.get(url) 
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Haetaan kuvaelementit
    kuvaElementit = soup.select('.nohover')
       
    for j in range(len(kuvaElementit)):
        kuvaURL = 'https://muusikoiden.net' + kuvaElementit[j].get('href')
        res_pic = requests.get(kuvaURL)
        res_pic.raise_for_status()
   
    # Ladataan vain kuvat, ei pelkkää muusikoiden.net urlia.
        if(len(kuvaURL) > 24):
            print('Downloading... %s' % (kuvaURL))

            # Tallennetaan se koneelle
            mediaFile = open(os.path.join(kansio, os.path.basename(kuvaURL)), 'wb')
            for chunk in res_pic.iter_content(100000000):
                mediaFile.write(chunk)
            mediaFile.close()
        
print('Kuvat ladattu, kiitos!')