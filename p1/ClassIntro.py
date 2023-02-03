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

print(k1.sisi)

k1.sisi = 100
print(k1.sisi)

print(k1.kelilingKubus())

k2 = Kubus.__new__(Kubus)
k2.sisi = 5
print(k2.sisi)
