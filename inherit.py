class Animal: #parent class
    def kingdom(self):
        print('saya adalah hewan')

class Mamalia(Animal): #child class
    def kelas(self):
        print('saya adalah mamalia')

class Aves(Animal): #child class
    def kelas(self):
        print('saya adalah aves')

class Carnivora(Mamalia): #grandchild class
    def ordo(self):
        print('saya pemakan daging')

kucing = Carnivora()
kucing.kingdom()
kucing.kelas()
kucing.ordo()

