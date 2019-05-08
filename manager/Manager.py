from files_stuff.Loader import Loader
from files_stuff.Saver import Saver
from manager.Painter import Painter


class Manager:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.crawlers_list = []
        self.painter = Painter(self.name, self.surname)
        self.saver = Saver()
        self.saver.placeholder_file_creator()
        self.crawlers_list = Loader.get_file_as_list("misc/crawler_names_list.txt")
        self.temp_painters_list = {}

    def run(self):
        #self.print_crawler_list()
        self.get_crawlers_data()

        self.saver.save_final_file(self.painter.text_dump())

    def add_temp_painter(self, painter):
        self.temp_painters_list.append(painter)

    def print_crawler_list(self):
        print("crawlers list:")

        if self.crawlers_list is []:
            print("pusto")
        else:
            for crawler in self.crawlers_list:
                print("["+crawler+"]")

    def get_crawlers_data(self):
        for crawler in self.crawlers_list:
            raw_data = Loader.get_file_raw("files_stuff/raw/"+crawler+".txt")
            self.painter.new_text(raw_data)

            interpreted_file_lines = Loader.get_file_as_list("files_stuff/interpreted/"+crawler+".txt")

            data_ur_list = self.explode_line(interpreted_file_lines[0])
            miejsce_ur_list = self.explode_line(interpreted_file_lines[1])
            data_sm_list = self.explode_line(interpreted_file_lines[2])
            miejsce_sm_list = self.explode_line(interpreted_file_lines[3])
            kategoria_list = self.explode_line(interpreted_file_lines[4])
            dzielo_list = self.explode_line(interpreted_file_lines[5])

            for dane in data_ur_list:
                self.painter.new_dictionary_entries(dane, "data_ur")

            for dane in miejsce_ur_list:
                self.painter.new_dictionary_entries(dane, "miejsce_ur")

            for dane in data_sm_list:
                self.painter.new_dictionary_entries(dane, "data_sm")

            for dane in miejsce_sm_list:
                self.painter.new_dictionary_entries(dane, "miejsce_sm")

            for dane in kategoria_list:
                self.painter.new_dictionary_entries(dane, "kategoria")

            for dane in dzielo_list:
                self.painter.new_dictionary_entries(dane, "dzielo")

    def explode_line(self, line):
        list = line.split(',')
        for element in list:
            element.strip()

        return list


