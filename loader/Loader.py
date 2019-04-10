class Loader:

    filename_base = ""
    next_file_no = 0

    def __init__(self, name, surname):
        self.filename_base = name + "_" + surname

    def get_next_file(self):
        contents = ""
        opened = True

        file_path = self.filename_base + "_" + str(self.next_file_no) + ".txt"
        try:
            f = open(file_path, "r")
        except IOError:
            opened = False

        if opened is True:
            contents = f.read()

        self.next_file_no += 1
        return contents
