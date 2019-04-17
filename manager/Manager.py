from files_stuff.Loader import Loader
from manager.Painter import Painter


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



