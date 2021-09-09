def getLength(a):
	count = 0
	firstLength = abs(ord("a") - ord(a[0]))
	if firstLength < 13:
		length = firstLength
	else:
		length = 26 - firstLength
	count += length
	for i in range(1,len(a)):
		nextLength = abs(ord(a[i]) - ord(a[i-1]))
		if nextLength < 13:
			length2 = nextLength
		else:
			length2 = 26 - nextLength
		count += length2
	return count

a = input()
print(getLength(a))