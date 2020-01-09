class CTitik():
	
	def __init__(self):
		self.x_all = []
		self.y_all = []

	def __setitem__(self, x, y):
		self.x_all.append(x)
		self.y_all.append(y)

	def __getitem__(self,x,y):
		if x in self.x:
			return self.y[self.x.index(x)]
		else:
			return none

	def tampil(self):
		print(self.x_all,self.y_all)

	def jarak(self):
		jarakx = abs(self.x_all[1]-self.x_all[0])
		jaraky = abs(self.y_all[1]-self.y_all[0])
		
		print(jarakx)

		print(jaraky)


class Cgaris(CTitik):
	def panjang(self):
		panjangx = abs(self.x_all[1]-self.x_all[0])
		panjangy = abs(self.y_all[1]-self.y_all[0])

		print((panjangx**2+panjangy**2)**0.5)


exa1 = CTitik()

exa1[11]=5
exa1[7]=8
exa1.tampil()
exa1.jarak()
print('')

exa2 = Cgaris()
exa2[11]=5
exa2[7]=8
exa2.tampil()
exa2.jarak()
exa2.panjang()