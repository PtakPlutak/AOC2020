f = open("input.txt", "r")
inp=f.readlines()
f.close()

spl=0
for idx, line in enumerate(inp):
    if line=="\n":
        spl=idx

pl1=[int(f) for f in inp[1:spl]]
pl2=[int(f) for f in inp[spl+2:]]

while len(pl1)!=0 and len(pl2)!=0:
    #print(pl1[0],pl2[0])
    if pl1[0]>pl2[0]:
        pl1.append(pl1[0])
        pl1.append(pl2[0])
    else:
        pl2.append(pl2[0])
        pl2.append(pl1[0])
    pl1.pop(0)
    pl2.pop(0)
    #print(pl1,pl2)

if len(pl1)!=0:
    pl=pl1
else:
    pl=pl2

i=1
sum=0

for x in list(reversed(pl)):
    sum=sum+x*i
    i=i+1

print(sum)