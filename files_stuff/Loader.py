class Loader:

    @staticmethod
    def get_file_data(file_path):
        contents = None
        opened = True

        try:
            f = open(file_path, "r")
        except IOError:
            opened = False

        if opened is True:
            contents = f.read()

        return contents
