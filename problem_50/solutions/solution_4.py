import sys

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int,minp().split()))

def solve():
	n = mint()
	a = list(mints())
	c = dict()
	c[0] = 2*n
	d = 0
	#print(d, end=' ')
	for i in range(2*n-1,n-1,-1):
		if a[i] == 1:
			d += 1
		else:
			d -= 1
		#print(d, i-n, end=' ')
		c[d] = i
	#print()
	d = 0
	r = 2*n
	r = min(r, n + c[0] - n)
	for i in range(n):
		if a[i] == 1:
			d += 1
		else:
			d -= 1
		#print(d, n-i-1, end=' ')
		if (-d) in c:
			r = min(r, n - i - 1 + c[-d] - n)
	#print()
	return r


for i in range(mint()):
	print(solve())

