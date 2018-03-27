T = int(raw_input())
while T:
    s = raw_input()
    if s == 'b' or s == 'B':
        print "BattleShip"
    elif s == 'c' or s == 'C':
        print "Cruiser"
    elif s == 'd' or s == 'D':
        print "Destroyer"
    else:
        print "Frigate"
    T -= 1
