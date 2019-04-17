class Painter:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.raw_texts = []
        self.data_ur = None

    def print(self):
        print()
        print("Name: ", self.name)
        print("Surname: ", self.surname)
        for keys, values in self.data_ur.items():
            print(keys)
            print(values)
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

    def new_birth_date(self, birth_date):
        if birth_date in self.data_ur:
            self.data_ur[birth_date] += 1
        else:
            self.data_ur[birth_date] = 1






