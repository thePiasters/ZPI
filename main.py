from manager.Manager import Manager
from crawlers import magazyn_sztuki as ms
from crawlers import wiki
import sys

def main():
    name = "Jan"
    surname = "Matejko"

    query = None
    if len(sys.argv) == 2:
        query = sys.argv[1]

    if query is not None:
        query_list = query.split(" ")
        if len(query_list) >= 2:
            name = query_list[0].strip()
            surname = query[len(name):].strip()

    manager = Manager(name, surname)

    #print(name +" "+ surname)

    #wiki.run(manager, "Aleksander", "Fredro")

    #wiki.run(manager, "Salvador", "Dali")
    #wiki.run(manager, name_query, surname_query)
    #iki.run(manager, "Salvador", "Dali")
    #wiki.run(manager, name_query, surname_query)
    #ms.find_painter_url(surname_query)

    wiki.run(manager, name, surname)
    ms.find_painter_url(manager, surname)
    manager.run()

if __name__ == "__main__":
    main()




