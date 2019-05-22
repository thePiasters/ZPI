import operator
import operator
import collections

class Painter:

    def __init__(self, crawler_name):
        self.name_query = ""
        self.surname_query = ""

        self.raw_texts = dict()
        self.temp_raw_text = ""

        self.name_dict = dict()
        self.name_temp_list = []

        self.birth_date_dict = dict()
        self.birth_date_temp_list = []

        self.birth_place_dict = dict()
        self.birth_place_temp_list = []

        self.death_date_dict = dict()
        self.death_date_temp_list = []

        self.death_place_dict = dict()
        self.death_place_temp_list = []

        self.category_dict = dict()
        self.category_temp_list = []

        self.work_dict = dict()
        self.work_temp_list = []

        self.museum_dict = dict()
        self.museum_temp_list = []

        self.education_dict = dict()
        self.education_temp_list = []

        self.link_dict = dict()
        self.link_temp_list = []

        self.dictionary_tags = {"imie", "data_ur", "miejsce_ur", "data_sm", "miejsce_sm", "dzielo", "kategoria", "muzeum", "studia", "link"}

        self.crawler_name = crawler_name

    def set_queries(self, name_query, surname_query):
        self.name_query = name_query
        self.surname_query = surname_query

    def crawler_text_dump(self):
        to_print = "~~~~~~~~~~~~~~~~~\nDANE Z CRAWLERA: "+self.crawler_name+"\n"
        to_print += self.print_temp_list("Name:", self.name_temp_list)
        to_print += self.print_temp_list("Birth Date:", self.birth_date_temp_list)
        to_print += self.print_temp_list("Birth Place:", self.birth_place_temp_list)
        to_print += self.print_temp_list("Death Date:", self.death_date_temp_list)
        to_print += self.print_temp_list("Death Place:", self.death_place_temp_list)
        to_print += self.print_temp_list("Categories:", self.category_temp_list)
        to_print += self.print_temp_list("Works:", self.work_temp_list)
        to_print += self.print_temp_list("Museum:", self.museum_temp_list)
        to_print += self.print_temp_list("Education:", self.education_temp_list)
        to_print += self.print_temp_list("Gallery:", self.link_temp_list)

        to_print += "~~~~~~~~~~~~~~~~~"
        return to_print

    def text_dump(self):
        end_line = "\n"
        to_print = "[QUERY]:"+end_line+self.name_query+" "+self.surname_query+end_line

        to_print += self.print_dictionary("[Name]:", self.name_dict)
        to_print += self.print_dictionary("[Birth Date]:", self.birth_date_dict)
        to_print += self.print_dictionary("[Birth Place]:", self.birth_place_dict)
        to_print += self.print_dictionary("[Death Date]:", self.death_date_dict)
        to_print += self.print_dictionary("[Death Place]:", self.death_place_dict)
        to_print += self.print_dictionary("[Categories]:", self.category_dict)
        to_print += self.print_dictionary("[Works]:", self.work_dict)
        to_print += self.print_dictionary("[Museum]:", self.museum_dict)
        to_print += self.print_dictionary("[Education]:", self.education_dict)

        to_print += end_line + end_line
        to_print += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + end_line
        to_print += "RAW TEXTS" + end_line
        to_print += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + end_line + end_line

        for crawler, text in self.raw_texts.items():
            to_print += "~~~~~~~~~~~~~" + end_line
            to_print += "SOURCE ["+crawler+"]"+end_line
            to_print += "~~~~~~~~~~~~~" + end_line
            to_print += text
            to_print += end_line + end_line

        to_print += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + end_line
        to_print += self.print_dictionary("GALLERY:", self.link_dict)

        return to_print

    def text_dump_list(self):
        end_line = "\n"

        to_print = self.print_dictionary("[Name]:", self.name_dict)
        to_print += self.print_dictionary("GALLERY:", self.link_dict)

        return to_print

    def print_temp_list(self, header, list):
        to_return = "\n" + header + "\n"

        if list is None:
            to_return += "[no data]" + "\n"
        else:
            index = 0
            for values in list:
                index += 1
                to_return += "["+values+"]"
                if index != len(list):
                    to_return += ", "
                else:
                    to_return += "\n"
        return to_return

    def print_dictionary(self, header, dictionary):
        to_return = "\n" + header + "\n"

        if bool(dictionary) is False:
            to_return += "<no data>" + "\n"
        else:
            for keys, values in dictionary.items():
                to_return += str(values)+" rep(s): "+'<'+keys+">" + "\n"
        return to_return

    def new_text(self, new_text):
        self.raw_texts[self.crawlers_name] = new_text

    def new_crawler_data_list(self, temp_list, tag):
        target_list = self.get_list_by_tag(tag)
        for element in temp_list:
            element_stripped = element.strip()
            target_list.append(element_stripped)

    def new_temp_text(self, text):
        self.temp_raw_text = text

    def new_dictionary_entries(self, list_data, list_name):
        if list_data is not []:
            dictionary = self.get_dictionary_by_tag(list_name)

            if dictionary is not None:
                for data in list_data:
                    if data is not "":
                        if data in dictionary:
                            dictionary[data] += 1
                        else:
                            dictionary[data] = 1

    def get_dictionary_by_tag(self, tag):
        dictionary = None
        if tag == "imie":
            dictionary = self.name_dict
        elif tag == "data_ur":
            dictionary = self.birth_date_dict
        elif tag == "miejsce_ur":
            dictionary = self.birth_place_dict
        elif tag == "data_sm":
            dictionary = self.death_date_dict
        elif tag == "miejsce_sm":
            dictionary = self.death_place_dict
        elif tag == "kategoria":
            dictionary = self.category_dict
        elif tag == "dzielo":
            dictionary = self.work_dict
        elif tag == "link":
            dictionary = self.link_dict
        elif tag == "muzeum":
            dictionary = self.museum_dict
        elif tag == "studia":
            dictionary = self.education_dict
        return dictionary

    def get_list_by_tag(self, tag):
        temp_list = []
        if tag == "imie":
            temp_list = self.name_temp_list
        elif tag == "data_ur":
            temp_list = self.birth_date_temp_list
        elif tag == "miejsce_ur":
            temp_list = self.birth_place_temp_list
        elif tag == "data_sm":
            temp_list = self.death_date_temp_list
        elif tag == "miejsce_sm":
            temp_list = self.death_place_temp_list
        elif tag == "kategoria":
            temp_list = self.category_temp_list
        elif tag == "dzielo":
            temp_list = self.work_temp_list
        elif tag == "link":
            temp_list = self.link_temp_list
        elif tag == "muzeum":
            temp_list = self.museum_temp_list
        elif tag == "studia":
            temp_list = self.education_temp_list
        return temp_list

    def add_data_from_temp_painter(self, temp_painter):
        temp_data_crawler = temp_painter.crawler_name

        self.raw_texts[temp_data_crawler] = temp_painter.temp_raw_text

        for tag in self.dictionary_tags:
            temp_list = temp_painter.get_list_by_tag(tag)
            self.new_dictionary_entries(temp_list, tag)

    def sort_dictionaries(self):
        for tag in self.dictionary_tags:
            dictionary = self.get_dictionary_by_tag(tag)
            sorted_x = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
            sorted_dictionary = collections.OrderedDict(sorted_x)

            dictionary.clear()
            dictionary.update(sorted_dictionary)






