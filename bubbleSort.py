def bubblesort(a):
	for i in range(len(a)):
		yield a
		for j in range(len(a)-i-1):
			if a[j]>a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
			yield a
	return a
# a=[int(i) for i in input().split()]
# for i in bubblesort(a):
# 	print(i)
