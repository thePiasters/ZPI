from manager.Manager import Manager
from crawlers import magazyn_sztuki as ms
from crawlers import wiki


def main():
    name_query = "Jan"
    surname_query = "Matejko"

    manager = Manager(name_query, surname_query)

    wiki.run(manager, "Aleksander", "Fredro")
    wiki.run(manager, name_query, surname_query)
    wiki.run(manager, "Salvador", "Dali")
    wiki.run(manager, name_query, surname_query)
    wiki.run(manager, "Salvador", "Dali")
    wiki.run(manager, name_query, surname_query)
    #ms.find_painter_url(surname_query)

    manager.run()

if __name__ == "__main__":
    main()




