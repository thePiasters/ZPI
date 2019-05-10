import requests
from bs4 import BeautifulSoup
from manager.Painter import Painter

months_and_syntax = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca',
                     'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia', 'ok.']


def run(manager, *names):
    painter = Painter("wikipedia")
    painter.new_temp_text(get_raw_text(*names))

    images = get_images(*names)
    painter.new_crawler_data_list(images, "link")

    soup = set_up_url(*names)

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

    print(painter.crawler_text_dump())
    manager.add_temp_painter(painter)


def set_up_url(*names):
    painter = format(*names)
    # *TODO: jak uzytkownik wpisze nie pelne imie i nazwisko;  modyfikacja/szukanie requesta
    url = 'https://pl.wikipedia.org/wiki/' + painter
    source_code = requests.get(url).text
    return BeautifulSoup(source_code, features="html.parser")


def format(*args):
    i = 0
    wiki_request_format = ''
    for n in args:
        wiki_request_format += n
        if i != len(args) - 1:
            wiki_request_format += '_'
        i = i + 1
    return wiki_request_format


def get_raw_text(*names):
    #file = open(path_raw, 'w', encoding='utf-8')
    soup = set_up_url(*names)

    raw_text = ""
    for component in soup.find_all('p' or 'h2' or 'h3'):
        raw_text += component.getText()
        #file.write(component.getText())

    return raw_text
    #file.close();



def concat(string, stirng_to_concat):
    if stirng_to_concat is not None:
        string += stirng_to_concat
    return string


def create_dictionary(path, *names, ):
    soup = set_up_url(*names)

    file = open(path, 'w', encoding='utf-8')
    string = "IMIĘ I NAZWSISKO: " + find_by_key_word(soup, 'Imię') + '\n'
    file.write(string)
    string = 'DATA URODZENIA: ' + extract_date(find_by_key_word(soup, 'urodzenia')) + '\n'
    file.write(string)

    string = 'DATA ŚMIERCI: ' + extract_date(find_by_key_word(soup, 'śmierci')) + '\n'
    file.write(string)
    string = 'MIEJCE URODZENIA: ' + extract_place(find_by_key_word(soup, 'urodzenia')) + '\n'
    file.write(string)
    string = 'MIEJCE ŚMIERCI: ' + extract_place(find_by_key_word(soup, 'śmierci')) + '\n'
    file.write(string)
    string = concat('Wykształcenie/uczelnia: ', find_by_key_word(soup, 'Alma Mater')) + '\n'
    file.write(string)

    string = 'Najwazniejsze dziela: '

    for art in find_work_of_arts(soup):
        string += art + ", "
    file.write(string)

    string = '\n Epoka: ' + find_by_key_word(soup, 'Epoka') + '\n'
    file.write(string)
    string = 'Muzeum artysty: ' + find_by_key_word(soup, 'Muzeum') + '\n'
    file.write(string)
    string = 'Pliki graficzne: \n '
    file.write(string)
    file.write(get_images(*names))
    file.close()


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
    component = soup.find('table', class_="infobox")
    paintings = []
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


def get_images(*names):
    soup = set_up_url(*names)
    components = soup.find_all('img')
    links_list = []
    for img in components:
        if "//upload.wikimedia" not in img['src'] or "svg" in img['src']:
            continue
        links_list.append(img['src'])

    return links_list;

