f = open("input.txt", "r")
inp=f.readlines()
f.close()

inp2=[]
for line in inp:
    line=line.replace("B","1")
    line=line.replace("F","0")
    line=line.replace("R","1")
    line=line.replace("L","0")
    curval=int(line,2)
    inp2.append(curval)

inp2.sort()
lastval=48
for tval in inp2:
    if tval-lastval>1:
        print(tval)
    lastval=tval