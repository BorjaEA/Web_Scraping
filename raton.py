URL='https://www.chollometro.com/categorias/logitech-mx-master-3s'

import requests
import pandas as pd
from bs4 import BeautifulSoup

r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

preciosYFechas = soup.find('div', attrs={'class':'cept-event-deals js-threadList listLayout-main'})

ofertas= []

meses = {
    "enero" : 1,
    "febrero" : 2,
    "marzo" : 3,
    "abril" : 4,
    "mayo" : 5,
    "junio" : 6,
    "julio" : 7
}

for row in preciosYFechas.find_all('div', attrs={'class':'threadGrid thread-clickRoot'}):
    oferta = {}
    
    precio = (row.find('span', attrs={'class':'thread-price text--b cept-tp size--all-l size--fromW3-xl text--color-greyShade'}).text[:-1]).replace(',','.')
    fecha = (row.find('span', attrs={'class':'hide--fromW3'}).text).replace('Publicado el ','')
    fecha = fecha.replace(' de ','')
    
    for mes in meses:

        if(fecha.find(mes)>=0):
            fecha = fecha.replace(mes,'/'+ str(meses[mes])+'/2023')


    oferta['precio'] = float(precio)
    oferta['fecha'] = fecha
    oferta['Nombre'] = row.find('a', attrs={'class':'cept-tt thread-link linkPlain thread-title--list js-thread-title'}).text
    oferta['url'] = row.find('a', attrs={'class':'cept-tt thread-link linkPlain thread-title--list js-thread-title', "href": True })['href']
    
    ofertas.append(oferta)
    

  
my_df = pd.DataFrame(ofertas)

my_df.to_csv('my_csv.csv', index=False, header=False)




