class Kubus:
    def __init__(self, sisi):

        self.__sisi = sisi


    @property
    def sisi(self):
        return self.__sisi

    @sisi.setter
    def sisi(self, sisi):
        self.__sisi = sisi
    
    def kelilingKubus(self):
        return 12 * self.__sisi


k1 = Kubus(10)


