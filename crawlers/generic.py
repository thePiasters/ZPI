import requests
from bs4 import BeautifulSoup

def create_query(*names):
    query = ""
    for name in names:
        query += name +" "

    query += "malarz"
    print(query)
    url = "https://www.google.com/search?q=" + query
    source_code = requests.get(url).text
    print(source_code)
    return BeautifulSoup(source_code, features="html.parser")

def get_raw(*names):
    soup = create_query(*names)

    urls = []
    for d in soup.find_all('div', class_="g"):
        a = d.find('a')['href'][7:].split('&')[0]
        if 'wikipedia' in a or 'facebook' in a or 'youtube' in a:
            continue
        if 'http' in a:
            urls.append(a)
        if len(urls) >= 3:
            break

    print(urls)


    for u in urls:
        try:
            print("[SOURCE]   "+u)
            source_code = requests.get(u).text
            soup = BeautifulSoup(source_code, features="html.parser")
            for p in soup.find_all('p' or 'span'):
                print(p.getText())
        except requests.ssl.SSLCertVerificationError:
            print("=============================CERT.ERR=============================================================")





#get_raw("Błażejewski Piotr")
get_raw("Chmielowiec Adam")
#get_raw("Dimitrowicz Aleksander")
#get_raw("Hałas Józef")
#get_raw("Jakubek Marek")
#get_raw("Jarodzka-Grzyb Bożena")
#get_raw("Jarodzki Konrad")
#get_raw("Jarodzki Paweł")
#get_raw("Jaroszewski Janusz")
#get_raw("Kapłański Jerzy")
#get_raw("Klimczak – Dobrzaniecki Andrzej")
#get_raw("Kortyka Stanisław")
#get_raw("Leszek Mickoś")
#get_raw("Lewandowski – Palle Paweł")
#get_raw("Liszkowski Witold")
#
# get_raw("Laura Pawela ")
# get_raw("Przemyslaw Kijas ")
# get_raw("Wojciech Pukocz")
# get_raw("Merkel Janusz")
# get_raw("Mikołajek Mariusz")
# get_raw("Minciel Eugeniusz")
# get_raw("Nitka Nikt Jolanta")
# get_raw("Nitka Zdzisław")
# get_raw("Skarbek Krzysztof")
# get_raw("Szewczyk Anna")
# get_raw("Szpakowska Kujawska Anna")
# get_raw("Trybalski Paweł")
# get_raw("Twardowski Lech")
# get_raw("Wałaszek Andrzej Krzysztof")
# get_raw("Wilk Urszula")
# get_raw("Wołczuk Marian")
