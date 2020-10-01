def solution(s):
	right = 0
	salutes = 0

	for l in s:
		if l == '>':
			right += 1
		if l == '<':
			salutes += right * 2
	return salutes
