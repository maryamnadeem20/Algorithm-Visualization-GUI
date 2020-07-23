def mergesort(A, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    # yield A

def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i in range(len(merged)):
        A[start + i] = merged[i]
        yield A

# a=[int(i) for i in input().split()]
# for i in mergesort(a, 0, len(a)-1):
#     print(i)




# def mergesort(a):
# 	if len(a)<=1:
# 		return a
# 	m=len(a)//2
# 	b=mergesort(a[:m])
# 	c=mergesort(a[m:])
# 	A=merge(b, c)
# 	return A
# def merge(B, C):
# 	d=[]
# 	while B and C:
# 		b=B[0]
# 		c=C[0]
# 		if b<=c:
# 			d.append(b)
# 			del B[0]
# 		else:
# 			d.append(c)
# 			del C[0]
# 	if B:
# 		for i in B:
# 			d.append(i)
# 			del i
# 	if C:
# 		for i in C:
# 			d.append(i)
# 			del i
# 	return d

# print(mergesort(a))