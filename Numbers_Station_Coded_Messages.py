def solution(l, t):
	for i in range(1,len(l)):
		l[i] = l[i-1] +l[i]
	d = dict()
	d[0] = 0
	for i, element in enumerate(l):
		if element - t in d:
			return [d[element-t], i]
		else:
			d[element] = i + 1
	return [-1, -1]
