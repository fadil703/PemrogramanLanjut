def Binary_search(data, target, low, high):
	if low > high:
		print('data tidak terdapat pada array')
	else:
		mid = (low+high) // 2
		if target == data[mid]:
			return mid
		elif target < data[mid]:
			return Binary_search(data, target, low, mid - 1)
		else:
			return Binary_search(data, target, mid + 1, high)

data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 14
low = 0
high = len(data)-1
print(Binary_search(data, target, low, high))

