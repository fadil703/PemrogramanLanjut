def linearSearch(sortedList, target):
  for i in range(len(sortedList)):
    if (sortedList[i] == target):
    	return i

  return -1
print(linearSearch([1,3,9,22],22))

