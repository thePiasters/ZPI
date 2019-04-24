from files_stuff.Loader import Loader
from manager.Painter import Painter
import misc.misc

class Manager:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.crawlers_list = []
        self.painter = None

    def run(self):
        self.crawlers_list = Loader.get_file_as_list("misc/crawler_names_list.txt")
        self.painter = Painter(self.name, self.surname)
        self.print_crawler_list()

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

            interpreted_file = Loader.get_file("files_stuff/interpreted/"+crawler+".txt")

            interpreted_file.readLine().strip()
            interpreted_file.readLine().strip()
            data_ur = interpreted_file.readLine().strip()
            miejsce_ur = interpreted_file.readLine().strip()
            data_sm = interpreted_file.readLine().strip()
            miejsce_sm = interpreted_file.readLine().strip()
            epoka = interpreted_file.readLine().strip()

            if data_ur is not None:
                self.painter.new_birth_date(data_ur)

