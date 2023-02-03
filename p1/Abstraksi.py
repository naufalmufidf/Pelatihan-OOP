from abc import ABC, abstractmethod #Import Library

class Vehicle(ABC): #Membuat kelas Vehicle dengan objek ABC (Abstract Base Class)
    def __init__(self, speed, year) -> None: #Membuat Contructor
        self.__speed = speed #Membuat atribut private
        self.__year = year
    
    @property #Membuat getter untuk atribut speed
    def speed(self): 
        return self.__speed

    @speed.setter #Membuat setter untuk atribut speed
    def speed(self,x):
        self.__speed = x

    @property #Membuat getter untuk atribut year
    def year(self): 
        return self.__year

    @year.setter #Membuat setter untuk atribut year
    def year(self,year):
        self.__year = year

    def start(self): #Membuat method non-abstrak
        print("Menjalankan Mesin")

    @abstractmethod #Membuat method abstrak
    def drive(self):
        pass

class Car(Vehicle): #Membuat subkelas Car dengan objek Vehicle
    def drive(self): #Membuat method drive
        print("Mobil sedang Berjalan")
        return super().drive()

car = Car(120, 2022) #Membuat Objek
print("Car's Year:",car.year) #Memanggil dan Menampilkan Method
print("Car's Speed:",car.speed)
print("--Setter Berubah--") 
car.year = 2023 #Mengubah setter
car.speed = 130 
print("Car's Year:",car.year) #Memanggil dan Menampilkan Method
print("Car's Speed:",car.speed)
car.drive()
car2 = Car.__new__(Car) #Membuat Objek dengan Konstruktor Kosong
car2.year = 2020 #Menentukan Atribut
car2.speed = 150
print("--Konstruktor Kosong--")
print("Car's Year:",car2.year) #Memanggil dan Menampilkan Method
print("Car's Speed:",car2.speed)

