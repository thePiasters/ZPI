class Painter:

    name = ""
    surname = ""
    texts = []

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print(self):
        print()
        print("Name: ", self.name)
        print("Surname: ", self.surname)
        self.print_all_texts()

    def same_name(self, name, surname):
        result = False

        if self.name == name and self.surname == surname:
            result = True

        return result

    def new_text(self, new_text):
        self.texts.append(new_text)

    def print_all_texts(self):
        print()
        for i in range(len(self.texts)):
            print("ZRODLO ", str(i), ":\n", self.texts[i])
