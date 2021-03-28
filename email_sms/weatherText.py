#! python3

import requests, bs4, textmyself, time

res = requests.get('https://weather.com/fi-FI/weather/today/l/FIXX0002:1:FI?Goto=Redirected')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
saatieto = soup.select('div[data-testid="wxPhrase"]')   # This tag gets the weather-info.
lampotila = soup.select('span[data-testid="TemperatureValue"]')     #This tag gets the temperature-info.

# Print the weater info 60 times, it refreshes it every 5 seconds.
i = 0
while i < 60:
    print(str(saatieto[0].getText()) + ', Lämpötila: ' + str(lampotila[0].getText()), end='\r')
    if(saatieto[0] == 'Sadetta' or saatieto[0] == 'Kevyttä sadetta'):
        textmyself.textmyself('Ota sateenavarjo mukaan! :)')
    time.sleep(5)
    i = i + 1