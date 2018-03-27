def main():
	n = int(raw_input())
	a = map(int,raw_input().split())
	a = sorted(a)
	for i in xrange(n-1):
		if not (-1 <= a[i] - a[i+1] <= 1):
			return "NO"
	return "YES"

t = int(raw_input())
while t:
	print main()
	t -= 1	