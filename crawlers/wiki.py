import requests
from bs4 import BeautifulSoup

months_and_syntax = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca',
                     'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia', 'ok.']


def set_up_url(*names):
    painter = format(*names)
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


def get_raw_text(path, *names):
    file = open(path, 'w', encoding='utf-8')
    soup = set_up_url(*names)


    for component in soup.find_all('p' or 'h2' or 'h3'):
        file.write(component.getText())
    file.close();

def concat(string, stirng_to_concat):
    if stirng_to_concat is not None:
        string +=stirng_to_concat
    return string


def create_dictionary(path, *names,):
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
        string += art+", "
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
    string =""
    for img in components:
        if "//upload.wikimedia" not in img['src'] or "svg" in img['src']:
            continue
        string += img['src'] +"\n"
    return string;

#create_dictionary("Jan", "Matejko")
#create_dictionary("Pablo", "Picasso")
#create_dictionary("Salvador", "Dali")
#create_dictionary("Claude", "Monet")
#create_dictionary("Paul", "Gauguin")
#create_dictionary("Amanda", "Lear")
#create_dictionary("Michał", "Anioł")


#create_dictionary( "dict.txt", "Rembrandt")
#create_dictionary("Leonardo", "da", "Vinci")
# create_dictionary("Vincent", "van", "Gogh")
get_raw_text("raw.txt", "Rembrandt")
