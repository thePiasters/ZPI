from files_stuff.Loader import Loader
from files_stuff.Saver import Saver
from manager.Painter import Painter


class Manager:

    def __init__(self, name_query, surname_query):
        self.name_query = name_query
        self.surname_query = surname_query

        self.main_painter = Painter("agregator")
        self.main_painter.set_queries(name_query, surname_query)

        self.saver = Saver()
        self.temp_painters_list = []

    def run(self):
        self.merge_painters()
        self.main_painter.sort_dictionaries()
        self.saver.save_final_file(self.main_painter.text_dump())

    def run_list(self):
        self.merge_painters()
        self.main_painter.sort_dictionaries()
        self.saver.save_final_file(self.main_painter.text_dump())

    def add_temp_painter(self, painter):
        self.temp_painters_list.append(painter)

    def merge_painters(self):
        for temp_painter in self.temp_painters_list:
            self.main_painter.add_data_from_temp_painter(temp_painter)


