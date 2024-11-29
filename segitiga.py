class Segitiga:
    def __init__(self, alas = 4, tinggi = 3, sisi1 = 5, sisi2 = 5):
        self.alas = alas
        self.tinggi = tinggi
        self.sisi1 = sisi1
        self.sisi2 = sisi2
        print('nilai atribut dari segitiga telah dimasukkan')
    
    def luas(self):
        hasilluas = 0.5 * self.alas * self.tinggi
        print('luas segitiga adalah = ', hasilluas)

    def keliling(self):
        hasilkeliling = self.alas + self.sisi1 +self.sisi2
        print('keliling segitiga adalah = ', hasilkeliling)

segitiga1 = Segitiga()
segitiga1.luas()
segitiga1.keliling()
segitiga2 = Segitiga()
segitiga2.luas()
segitiga2.keliling()