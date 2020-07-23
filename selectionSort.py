def selection(a):
	for i in range (len(a)):
		minIndex=i
		for j in range(i+1, len(a)):
			if a[j]<a[minIndex]:
				minIndex=j
			yield a
		a[i], a[minIndex]=a[minIndex], a[i]
		yield a