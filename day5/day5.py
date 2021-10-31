f = open("input.txt", "r")
inp=f.readlines()
f.close()

maxval=0

for line in inp:
    line=line.replace("B","1")
    line=line.replace("F","0")
    line=line.replace("R","1")
    line=line.replace("L","0")
    curval=int(line,2)
    if maxval<curval:
        maxval=curval
        
print(maxval)