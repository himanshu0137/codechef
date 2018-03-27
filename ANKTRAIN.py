t = int(raw_input())
func = [(-1,"SL"),(3,"LB"),(3,"MB"),(3,"UB"),(-3,"LB"),(-3,"MB"),(-3,"UB"),(1,"SU")]
while t:
    n = int(raw_input())
    count = 0
    x = n%8
    print "{}{}".format(n+func[x][0],func[x][1])
    t -= 1