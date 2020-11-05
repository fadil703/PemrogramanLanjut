import timeit
def methodNo22(n):
	if n==0:
		return 0
	return n*n +methodNo22(n-1)

def methodNo2(n):
	s = 0
	for i in range(1,n+1):
		s = s+i*i
	return s

t = timeit.timeit('methodNo2(20)', 'from __main__ import methodNo2')
t2 = timeit.timeit('methodNo22(20)', 'from __main__ import methodNo22')

print(methodNo2(20))
print(methodNo22(20))
print(t)
print(t2)
