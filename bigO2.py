import timeit
def fact2(n):
    if n == 0:
        return 1
    else:
        return n * fact2(n-1)

t = timeit.timeit('fact2(50)', 'from __main__ import fact2')
print(fact2(50))
print(t)