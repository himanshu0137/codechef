def func(n):
    if n == 2:
        return "2"
    if n == 0:
        return "0"
    array = []
    j = 0
    while n:
        if n&1:
            array.append(j)
        n = n>>1
        j += 1
    array.reverse()
    ans = ""
    for j in array:
        if j == 1:
            ans += "2+"
        else:
            ans += "2(" + func(j) + ")+"
    return ans[:-1]
Numbers = [137, 1315, 73, 136, 255, 1384, 16385]
for i in Numbers:
    print "{}={}".format(i,func(i))
