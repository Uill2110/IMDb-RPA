import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_film_data(link):
    pagina = requests.get(link)
    conteudo = pagina.content
    soup = BeautifulSoup(conteudo, 'html5lib')  
    image = soup.img.get_attribute_list('src')[0]
    titulo = soup.find("h1",{"data-testid":"hero-title-block__title"}).text

    art = [x.text for x in soup.select("li[data-testid='title-pc-principal-credit']:nth-child(3) > div > ul > li")]
    arts = " - ".join(list(set(art)))
    
    return image, titulo, arts