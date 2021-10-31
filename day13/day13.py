f = open("input.txt", "r")
inp=f.readlines()
f.close()
inp2=[]

for i in inp[1].split(","):
    if i=="x":
        inp2.append(-1)
    else:
        inp2.append(int(i))

st=int(inp[0])
#k=59
#print(k-st%k)
minVal=1000
minValB=0
for numB in inp2:
    if numB>0:
        if minVal>(numB-st%numB):
            minVal=numB-st%numB
            minValB=numB

print(minValB*minVal)