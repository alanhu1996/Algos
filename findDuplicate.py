def findDuplicate(array):
	result = []
	for i in array:
		if(i < 0):
			result.append(-i)
		else:
			array[i] = -1 * array[i]
	zeroFound = False
	for i in array:
		if zeroFound:
			result.append(0)
		elif i == 0:
			zeroFound = True
	return result


print(findDuplicate([1,2,2,3,5,5,0,0]))	