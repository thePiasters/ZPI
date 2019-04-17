from loader.LoaderMain import LoaderMain
from crawlers import magazyn_sztuki as ms

def main():
    name = "Zdzislaw"
    surname = "Beksinski"

    ms.find_painter_url('vinci')
    #f = open('..\ZPI\loader\magazyn_sztuki_0.txt','w')
    #f.write('c')
    loader = LoaderMain(name, surname)
    loader.run()
    #f.close()


if __name__ == "__main__":
    main()




