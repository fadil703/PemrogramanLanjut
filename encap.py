class Encaps:
    def __init__(self):

        self.a = 'public variable'   #variabel publik
        self.__b = 'private variable' #variabel private

    def printEncap(self):
        print(self.a)  #memanggil variable publik
        print(self.__b)  #memanggil variable private

E = Encaps()
print(E.a) # hasilnya public varible
#print(E.__b) # hasilnya akan error

print(E._Encaps__b) # menampilkan private variable