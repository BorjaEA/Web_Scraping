URL='https://www.chollometro.com/categorias/logitech-mx-master-3s'

import requests
from bs4 import BeautifulSoup

r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

preciosYFechas = soup.find('div', attrs={'class':'cept-event-deals js-threadList listLayout-main'})

ofertas= []

for row in preciosYFechas.find_all('div', attrs={'class':'threadGrid thread-clickRoot'}):
    oferta = {}
    precio = (row.find('span', attrs={'class':'thread-price text--b cept-tp size--all-l size--fromW3-xl text--color-greyShade'}).text[:-1]).replace(',','.')
    
    oferta['precio'] = float(precio)
    oferta['fecha'] = row.find('span', attrs={'class':'hide--fromW3'}).text
    oferta['Nombre'] = row.find('a', attrs={'class':'cept-tt thread-link linkPlain thread-title--list js-thread-title'}).text
    oferta['url'] = row.find('a', attrs={'class':'cept-tt thread-link linkPlain thread-title--list js-thread-title', "href": True })['href']
    
    ofertas.append(oferta)
    
    
  

for row in ofertas:
    print(row)

