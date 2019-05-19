import requests
from bs4 import BeautifulSoup
from google.cloud import translate


url_search_counter = 3

def create_query(*names):
    query = ""
    for name in names:
        query += name + " "

    query += "touchofart"

    url = "https://www.google.com/search?q=" + query
    source_code = requests.get(url).text
    return BeautifulSoup(source_code, features="html.parser")


def get_raw_text(*names):
    soup = create_query(*names)

    url = ""
    for d in soup.find_all('div', class_="g"):
        a = d.find('a')['href']
        if "touchofart.eu" not in a or "https://www.touchofart.eu/en" in a or "https://www.touchofart.eu/ru" in a or 'galeria' in a or "https://www.touchofart.eu/de" in a:
            continue
        a = a.replace("/url?q=https://www.touchofart.eu/", "")
        a = a.split("/")
        url = "https://www.touchofart.eu/" + a[0]
        break

    if url == "":
        if url_search_counter > 0:
            print(url_search_counter)
            --url_search_counter
            print(url_search_counter)
            get_raw_text(*names)
        else:
            print("??????????")
            return


    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")

    raw_text = ""
    for component in soup.find_all('article'):
        raw_text += component.getText()
        # file.write(component.getText())


    return get_translation(raw_text)

def get_translation(text):
    # Instantiates a client
    translate_client = translate.Client()

    # The target language
    target = 'pl'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    return format(translation['translatedText'])


#
# print(get_raw_text("Eugenion", "Berti"))
print(get_raw_text("Twoja Stara"))