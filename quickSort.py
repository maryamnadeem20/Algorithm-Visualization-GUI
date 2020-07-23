# a=[int(i) for i in input().split()]

def quicksort(a, l, r):
	if l>=r:
		return 
	x=a[l]
	j=l
	for i in range(l+1, r+1):
		if a[i]<=x:
			j+=1
			a[j], a[i] = a[i], a[j]
		yield a
	a[l], a[j]=a[j], a[l]
	yield a
	yield from quicksort(a, l, j-1)
	yield from quicksort(a, j+1, r)

# a=[int(i) for i in input().split()]
# for i in quicksort(a, 0, len(a)-1):
#     print(i)


# def quicksort(a, l, r):
# 	if l<r:
# 		m=partition(a, l, r)
# 		yield from quicksort(a, l, m-1)
# 		yield from quicksort(a, m+1, r)

# def partition(a, l, r):
# 	x=a[l]
# 	j=l
# 	for i in range(l+1, r+1):
# 		if a[i]<=x:
# 			j+=1
# 			a[j], a[i] = a[i], a[j]
# 		yield a
# 	a[l], a[j]=a[j], a[l]
# 	yield a
# 	return j
