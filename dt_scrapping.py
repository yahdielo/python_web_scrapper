import requests
from bs4 import BeautifulSoup
import pandas as pd

#url to get charizard vmax trading cards finalize sells data from ebay
url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=charizard+vmax+rainbow+psa+10&_sacat=0&LH_TitleDesc=0&Grade=10&_oaa=1&_dcat=183454&LH_BO=1&rt=nc&LH_Sold=1&LH_Complete=1"

def  get_data(url):
    """
    this module takes url as parameter, and creats a soup object
    and returns it
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup

def parse(soup):
    """
    this module calls find all method in suop object, and pass parameters 
    div and soecific class to look in to
    """
    resutls = soup.find_all('div', {'class': 's-item__info clearfix'})
    for items in resutls:
        products = {
            'title' : items.find('div', {'class': 's-item__title'}).text,
            'date_sold' : items.find('span', {'class': 's-item__title--tagblock'}),
            'sold_price' : float(items.find('span', {'class': 's-item__price'}).text.replace('USD', '').replace('$', ''))
        }
        print(products)
    return

soup = get_data(url)
parse = parse(soup)