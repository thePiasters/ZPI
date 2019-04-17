#stringi: name, surname, data_ur, miejsce_ur, miejsce_sm, data_sm, epoka
#tablice stringow: style, dziela
#jak brak danych to puste stringi (albo tablice)
def get_interpreted_file_template(data_ur, miejsce_ur, data_sm, miejsce_sm, kategorie, dziela):
    newline = "\n"
    delimiter = ","

    template = data_ur + newline + miejsce_ur + newline + data_sm + newline + miejsce_sm + newline

    for kategoria in kategorie:
        template += kategoria + delimiter
    template += newline

    for dzielo in dziela:
        template += dzielo + delimiter
    template += newline

    template += newline

    return template;


def get_data_from_template_file(file):
    name = file.readLine().strip()
    surname = file.readLine().strip()
    data_ur = file.readLine().strip()
    miejsce_ur = file.readLine().strip()
    data_sm = file.readLine().strip()
    miejsce_sm = file.readLine().strip()
    epoka = file.readLine().strip()


    return (name, surname, data_ur, miejsce_ur, data_sm, miejsce_sm, epoka)