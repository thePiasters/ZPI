import requests
from bs4 import BeautifulSoup
from manager.Painter import Painter

months_and_syntax = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca',
                     'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia', 'ok.']

key_words =['Malarze', 'malarze']

categories = []


def run(*names):


    painter = Painter("wikipedia")
    painter.new_temp_text(get_raw_text(soup))

    name = find_by_key_word(soup, 'Imię')
    painter.new_crawler_data_list({name}, "imie")

    data_ur = extract_date(find_by_key_word(soup, 'urodzenia'))
    painter.new_crawler_data_list({data_ur}, "data_ur")

    miejsce_ur = extract_place(find_by_key_word(soup, 'urodzenia'))
    painter.new_crawler_data_list({miejsce_ur}, "miejsce_ur")

    data_sm = extract_date(find_by_key_word(soup, 'śmierci'))
    painter.new_crawler_data_list({data_sm}, "data_sm")

    miejsce_sm = extract_place(find_by_key_word(soup, 'śmierci'))
    painter.new_crawler_data_list({miejsce_sm}, "miejsce_sm")

    dziela = find_work_of_arts(soup)
    painter.new_crawler_data_list(dziela, "dzielo")

    kategorie = []
    epoka = find_by_key_word(soup, 'Epoka')

    if epoka != "":
        kategorie.append(epoka)

    painter.new_crawler_data_list(kategorie, "kategoria")


    muzea = []
    muzeum = find_by_key_word(soup, 'Muzeum artysty')
    if muzeum != "":
        muzea.append(muzeum)

    painter.new_crawler_data_list(muzea,"muzeum")

    edukacja = []
    edu = find_by_key_word(soup, 'Alma Mater')
    edu_1 = find_by_key_word(soup,"Uczelnia")
    if edu != "":
        edukacja.append(edu)
    if edu_1 != '':
        edukacja.append(edu_1)

    painter.new_crawler_data_list(edukacja, "studia")
    print(painter.crawler_text_dump())
    # manager.add_temp_painter(painter)


def set_up_url(*names):

    url = get_url(*names)
    if check_if_url_is_correct(url):
        source_code = requests.get(url).text
        return BeautifulSoup(source_code, features="html.parser")
    else:
        return None


def get_raw_text(soup):


    if soup is None:
        return ""

    raw_text = ""
    for component in soup.find_all('p' or 'h2' or 'h3'):
        raw_text += component.getText()

    return raw_text



def extract_date(string):
    if string is not None:
        date = ''
        table = string.split()
        for i in table:
            if i.isdigit() or months_and_syntax.count(i) > 0:
                date += i
                date += ' '
        return date


def extract_place(string):
    if string is not None:
        place = ''
        table = string.split()
        for i in table:
            if months_and_syntax.count(i) == 0 and not i.isdigit():
                place += i
                place += ' '
        return place


def find_by_key_word(soup, keyword):
    if soup is not None:
        component = soup.find('table', class_="infobox")
        if component is not None:
            for child in component.find_all('tr'):
                if child.getText().find(keyword) != -1:
                    for i in child.find_all('td'):
                        if i.getText().find(keyword) == -1:
                            if i.getText() is not None:
                                return i.getText()
    return ""


def find_work_of_arts(soup):
    paintings = []
    if soup is not None:
        component = soup.find('table', class_="infobox")
        contains_header = False
        if component is not None:
            for child in component.find_all('tr'):
                if child.getText().find('Ważne dzieła') != -1:
                    contains_header = True
                if contains_header:
                    for i in child.find_all('i'):
                        if i is not None:
                            if i.find('a') is not None:
                                paintings.append(i.find('a').getText())
    return paintings


# def get_images(*names):
#     soup = set_up_url(*names)
#     components = soup.find_all('img')
#     links_list = []
#     for img in components:
#         if "//upload.wikimedia" not in img['src'] or "svg" in img['src']:
#             continue
#         links_list.append(img['src'])
#
#     return links_list

def create_query(*names):
    query = ""
    for name in names:
        query += name + " "

    query += "wikipedia"
    print(query)
    url = "https://www.google.com/search?q=" + query
    source_code = requests.get(url).text
    return BeautifulSoup(source_code, features="html.parser")

def check_if_category_contains_key_word(category):
    for key in key_words:
        if key in category:
            return True
    return False


def get_url(*names):
    soup = create_query(*names)
    url = ""

    # print("urls: ")
    # for d in soup.find_all('div', class_="g"):
    #     if d is not None:
    #         a = d.find('a')
    #         if a is not None:
    #             a = d.find('a')['href']
    #             if 'pl.wikipedia'in a:
    #                 a = a.replace("/url?q=", "")
    #                 print(a)
    #                 break

    for c in soup.find_all('cite'):
        if 'pl.wikipedia' in c.getText() and 'Kategoria' not in c.getText():
            url = c.getText()
            break

    if "http" not in url:
        print("Nie znalazł url")
        print("NIE MALARZ")
        return ""

    print(url)
    return url

def check_if_url_is_correct(url):



    print("checking url ", url)
    if url == "":
        return False

    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")

    div = soup.find(id="mw-normal-catlinks")
    if div is None:
        print("Nie znalazł kategorii dziad")
        print("NIE MALARZ")
        return False

    for a in div.find_all('a'):
        if check_if_category_contains_key_word(a.getText()):
            print("MALARZ")
            return True

    print("NIE MALARZ")
    return False
    #print(div)


# run("Wiktor Gajda")
# print("=====================================")
# run("Leonardo", "da", "Vinci")
# print("=====================================")
# run("Zdzislaw Beksinski")
# print("=====================================")
# run("Zofia Albinowska-Minkiewiczowa")
# print("=====================================")
# run("Witkacy")
# print("=====================================")
# run("Witold Cichacz")
# print("=====================================")
# run("Aniela Cukier")
# print("=====================================")
# run("Henryk Dębicki")
# print("=====================================")
# run("Antyfilos")
# print("=====================================")
# run("Fernando Botero Angulo")
# print("=====================================")
# run("Stanislaw Ignacy", "Witkiewicz")
# print("=====================================")
#
# run("Twoja Stara")
# print("=====================================")
#
# run("Michael Jackson")
# print("=====================================")
# run("Kurt Cobain")
# print("=====================================")
# run("Lech Kaczynski")
# print("=====================================")
# run("Rick Sanchez")
# print("=====================================")
# run("Dziaba dziaba")
# run("raptapapap")
# run("ja pierdole")
# run("ziemniaki")
# run("malarz")
# run("malarze","polscy")
# run("wojciech", "pukocz")

