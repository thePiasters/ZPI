from manager.Manager import Manager
from crawlers import magazyn_sztuki as ms
from crawlers import wiki


def main():
    name = "Zdzisław"
    surname = "Beksiński"

    wiki.run("Pablo", "Picasso")
    ms.find_painter_url(surname)

    manager = Manager(name, surname)
    manager.run()

if __name__ == "__main__":
    main()




