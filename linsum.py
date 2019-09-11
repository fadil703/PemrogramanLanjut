def Linear_sum(S, n):
	if n == 0:
		return 0
	else:
		return Linear_sum(S, n-1) + S(n-1)

S = [4,3,6,2,8]
n = 5
result = Linear_sum(S, n)
print(result)
