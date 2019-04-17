from Loader import Loader
from Painter import Painter


class Manager:

    painters = []

    def new_data(self, name, surname):
        loader = Loader(name, surname)

        painter = self.get_painter_by_name(name, surname)

        if painter is None:
            new_painter = Painter(name, surname)
            self.painters.append(new_painter)

        next_file = loader.get_next_file()
        while next_file != "":
            new_painter.new_text(next_file)
            next_file = loader.get_next_file()

    def run(self):
        self.new_data("Zdzislaw", "Beksinski")
        self.print_painters()

    def get_painter_by_name(self, name, surname):
        painter = None
        i = 0

        while Painter is None and i < len(self.painters):
            if self.painters[i].same_name(name, surname):
                painter = self.painters[i]
                i += 1

        return painter

    def print_painters(self):
        for i in range(len(self.painters)):
            self.painters[i].print()

