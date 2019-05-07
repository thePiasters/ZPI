class Saver:

    def save_interpreted_file(self, crawler_name, interpreted_template):

        file = open("files_stuff/interpreted/"+crawler_name+".txt", "w")
        file.write(interpreted_template)
        file.close

    def get_interpreted_file_template(self, data_ur, miejsce_ur, data_sm, miejsce_sm, kategorie, dziela):
        template = ""
        template += self.new_file_line(data_ur)
        template += self.new_file_line(miejsce_ur)
        template += self.new_file_line(data_sm)
        template += self.new_file_line(miejsce_sm)
        template += self.new_file_line(kategorie)
        template += self.new_file_line(dziela)

        template += "\n"

        return template

    def new_file_line(self, list):
        line = ""
        newline = "\n"
        delimiter = ","

        for element in list:
            line += element + delimiter

        line += newline
        return line

    def get_file_as_list(self, file_path):
        contents = []
        opened = True

        try:
            f = open(file_path, "r")
        except IOError:
            opened = False

        if opened is True:
            contents = f.readlines()

        counter = 0
        for line in contents:
            contents[counter] = line.strip()
            counter += 1

        return contents

    def save_final_file(self, data):
        file = open("files_stuff/result/result.txt", "w", encoding='utf-8')
        file.write(data)
        file.close

    def placeholder_file_creator(self):

        #plik1
        data_ur_list1 = {"1701", "1702"}
        miejsce_ur_list1 = {"Lebork"}
        miejsce_sm_list1 = {"Warsaw", "Poland"}
        dziela_list1 = {"costam", "costam2", "monalisa",  "bulka"}

        #data_ur, miejsce_ur, data_sm, miejsce_sm, kategorie, dziela
        template = self.get_interpreted_file_template(data_ur_list1, miejsce_ur_list1, [], miejsce_sm_list1, [], dziela_list1)
        self.save_interpreted_file("placeholder_crawler1", template)

        #plik2
        data_ur_list2 = {"1701"}
        miejsce_ur_list2 = {"Lebork"}
        data_sm_list2 = {"1765"}
        miejsce_sm_list2 = {"Poland"}
        dziela_list2 = {"costam", "monalisa"}

        template = self.get_interpreted_file_template(data_ur_list2, miejsce_ur_list2, data_sm_list2, miejsce_sm_list2, [], dziela_list2)
        self.save_interpreted_file("placeholder_crawler2", template)

        #plik3
        miejsce_ur_list3 = {"Lebork"}
        data_sm_list3 = {"1766"}
        miejsce_sm_list3 = {"Wroclaw"}
        kategoria_list3 = {"impresjonizm", "costam1", "plakat"}
        dziela_list3 = {"costam", "monalisa"}

        template = self.get_interpreted_file_template([], miejsce_ur_list3, data_sm_list3, miejsce_sm_list3, kategoria_list3, dziela_list3)
        self.save_interpreted_file("placeholder_crawler3", template)
