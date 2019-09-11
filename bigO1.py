import timeit
def fact(n):
	product = 1
	for i in range(n):
		product = product *(i+1)
	return product

t = timeit.timeit('fact(50)', 'from __main__ import fact')
print(fact(50))
print(t)