import timeit
def methodNo2(n):
	s = 0
	for i in range(1,n+1):
		s = s+i*i
	return s

t = timeit.timeit('methodNo2(5)', 'from __main__ import methodNo2')

print(methodNo2(5))
print(t)