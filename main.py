from manager.Manager import Manager
from crawlers import magazyn_sztuki as ms
from crawlers import wiki


def main():
    name = "Zdzisław"
    surname = "Beksiński"

    wiki_painter = wiki.run(name, surname)
    ms.find_painter_url(surname)

    manager = Manager(name, surname)
    manager.add_temp_painter(wiki_painter)


    manager.run()

if __name__ == "__main__":
    main()




