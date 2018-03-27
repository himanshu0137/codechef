from sys import stdin,stdout
stdout.write("1\n3 1 2 2\n3 3 4 4\n")
stdout.flush()
n = stdin.readline().strip()
d = {'0':'5','1':'1','2':'2','-1':'3','-2':'4'}
stdout.write("2\n"+d[n]+"\n")