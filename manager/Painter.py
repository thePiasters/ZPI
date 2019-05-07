class Painter:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.raw_texts = []
        self.birth_date_dict = dict()
        self.birth_place_dict = dict()
        self.death_date_dict = dict()
        self.death_place_dict = dict()
        self.category_dict = dict()
        self.work_dict = dict()

    def text_dump(self):
        end_line = "\n"

        to_print = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + end_line
        to_print += "BIO" + end_line
        to_print += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + end_line + end_line

        to_print += "[Name]:"+end_line+self.name+end_line
        to_print += end_line + "[Surname]:"+end_line+self.surname+end_line

        to_print += self.print_dictionary("[Birth Date]:", self.birth_date_dict)
        to_print += self.print_dictionary("[Birth Place]:", self.birth_place_dict)
        to_print += self.print_dictionary("[Death Date]:", self.death_date_dict)
        to_print += self.print_dictionary("[Death Place]:", self.death_place_dict)
        to_print += self.print_dictionary("[Categories]:", self.category_dict)
        to_print += self.print_dictionary("[Works]:", self.work_dict)

        to_print += end_line + end_line
        to_print += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + end_line
        to_print += "RAW TEXTS" + end_line
        to_print += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + end_line + end_line

        for i in range(len(self.raw_texts)):
            to_print += "~~~~~~~~~~~~~" + end_line
            to_print += "SOURCE "+str(i)+end_line
            to_print += "~~~~~~~~~~~~~" + end_line
            to_print += self.raw_texts[i]
            to_print += end_line + end_line

        return to_print

    def print_dictionary(self, header, dictionary):
        to_return = "\n" + header + "\n"

        if dictionary is None:
            to_return += "no data" + "\n"
        else:
            for keys, values in dictionary.items():
                to_return += keys + " - " + str(values) + " occurrences" + "\n"
        return to_return

    def new_text(self, new_text):
        self.raw_texts.append(new_text)

    def new_dictionary_entries(self, data, list_name):
        if data != "":
            dictionary = None
            set = True
            if list_name == "data_ur":
                dictionary = self.birth_date_dict
            elif list_name == "miejsce_ur":
                dictionary = self.birth_place_dict
            elif list_name == "data_sm":
                dictionary = self.death_date_dict
            elif list_name == "miejsce_sm":
                dictionary = self.death_place_dict
            elif list_name == "kategoria":
                dictionary = self.category_dict
            elif list_name == "dzielo":
                dictionary = self.work_dict
            else:
                set = False

            if set:
                if dictionary is not None and data in dictionary:
                     dictionary[data] += 1
                else:
                     dictionary[data] = 1






