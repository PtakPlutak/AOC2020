f = open("input.txt", "r")
inp=f.readlines()
f.close()
inp2=[]
for i in inp:
    inp2.append(int(i))
    
inp2.sort()
k=len(inp2)

diff1=0
diff2=0
diff3=0
involt=0

for i in range(k):
    k2=inp2[i]-involt
    involt=inp2[i]
    if k2==1:
        diff1+=1
    elif k2==2:
        diff2+=1
    elif k2==3:
        diff3+=1
diff3+=1
print(diff1,diff2,diff3)
print(diff1*diff3)