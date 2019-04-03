import requests
from bs4 import BeautifulSoup


def find_smth(first_name, last_name):
    painter = first_name + '_' + last_name
    url = 'https://pl.wikipedia.org/wiki/' + painter
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for p in soup.find_all('p'):
        print(p.getText())


