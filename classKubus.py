from multipledispatch import dispatch as ds

class Kubus:
    
    @ds()
    def __init__(self) -> None:
        self.__sisi = 5

    @ds(int)
    def __init__(self, sisi):
        self.__sisi = sisi

    @property
    def sisi(self):
        return self.__sisi

    @sisi.setter
    def sisi(self, sisi):
        self.__sisi = sisi

    @sisi.deleter
    def sisi(self):
        del self.__sisi

    def kelilingKubus(self):
        return 12 * self.__sisi


class Lingkaran:
    def __init__(self, jari):
        self.jari = jari

    