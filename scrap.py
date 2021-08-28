import json
import requests
from bs4 import BeautifulSoup

URL_mubawab = "https://www.mubawab.ma/fr/a/7215667/appartement-%C3%A0-hay-chrifa-bd-al-qods"
URL_avito = "https://www.avito.ma/fr/la_ville_haute/appartements/Appartement_en_Vente_%C3%A0_K%C3%A9nitra_46812563.htm"
URL_sarouty = "https://www.sarouty.ma/louer/villa-a-louer-marrakech-agdal-819702.html"


def del_from_list(A,element):
    new_a = []
    for el in A : 
        if element in el:
            continue
        new_a.append(el)
    return new_a

def mubawab(URL,output_name = 'mubawab.json'):
    output_scraped = {}
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    # Request
    mydivs = soup.find_all("span", {"class": "tagProp"})
    names = ['Surface','N° de Pièces','N° de Chambres','N° de Salles de bain','Etat','Ancieneté','Etage']
    price_div = soup.find("h3", {"class": "orangeTit"})
    search_title = soup.find("h1", {"class": "searchTitle"})
    Characteristics = soup.find("div", {"class": "catNav"})
    li = Characteristics.text.strip().split('\n')
    # Output
    output_scraped['Titre'] = search_title.text.strip()
    output_scraped['Prix'] = price_div.text.strip()
    new_li = del_from_list(li,'\t\t')

    for el,name in zip(new_li,names):
        output_scraped[name] = el

    return output_scraped

def avito(URL):

    # charac_list = []
    names_char = ['Surface','N° de Chambres','N° de Salles de bain']
    names_char_2  = ['Type','Secteur','Salons','Étage']
    output_scraped = {}
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Requêtes 
    mydivs = soup.find("div", {"class": "sc-1g3sn3w-7 eDUytn"})
    charac = soup.find("div", {"class": "sc-6p5md9-0 jTtIhf"})
    charac_2 = soup.find("ol", {"class": "qmn92k-2 kekZFG"})
    price_div = soup.find("p", {"class": "sc-1x0vz2r-0 eXteHH"})
    search_title = soup.find("h1", {"class": "sc-1x0vz2r-0 EJoJb"})

    # Output
    output_scraped['Titre'] = search_title.text.strip()
    output_scraped['Prix'] = price_div.text.strip()
    for el,name in zip(charac_2,names_char_2):
        output_scraped[name] = el.text.strip().split(name)[1]
    for el,name in zip(charac,names_char):
        output_scraped[name] = el.text.strip()

    return output_scraped #, charac_list


def sarouty(URL):
    
    output_scraped = {}
    names = ['Prix','Type','Référence','N° de Pièces','N° de Salles de bain','Mobiliers','Surface']
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Requêtes 
    charac = soup.find_all("div", {"class": "facts__content"})
    search_title = soup.find("h1", {"class": "property-header__title--detail"})

    # Output
    output_scraped['Titre'] = search_title.text.strip()

    for el,name in zip(charac,names):
        output_scraped[name] = el.text.strip()

    return output_scraped



    
# print(avito(URL_avito))
# print(sarouty(URL_sarouty))

