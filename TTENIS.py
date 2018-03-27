def check(s):
	w = 0
	l = 0
	i = 0
	while i < len(s):
		if w == 11:
			return "WIN"
		if l == 11:
			return "LOSE"
		if w == 10 and l == 10:
			return lastcheck(s[i+1:])
		if s[i] == "1":
			w += 1
		else:
			l += 1
		i += 1
	if w > l:
		return "WIN"
	else:
		return "LOSE"

def lastcheck(s):
	for i in xrange(len(s)):
		if s[i] == "1" and s[i+1] == "1":
			return "WIN"
		elif s[i] == "0" and s[i+1] == "0":
			return "LOSE"
def main():
	t = int(raw_input())
	while t:
		s = raw_input()
		print check(s)
		t -= 1
		
main()