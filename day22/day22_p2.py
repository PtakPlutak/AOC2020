f = open("input.txt", "r")
inp=f.readlines()
f.close()

spl=0
for idx, line in enumerate(inp):
    if line=="\n":
        spl=idx

sub1=[int(f) for f in inp[1:spl]]
sub2=[int(f) for f in inp[spl+2:]]
playDict={}

def playGame(pl1,pl2):
    global playDict
    i=0
    playStr="".join([str(elem) for elem in pl1])
    playStr=playStr.join("x")
    playStr=playStr.join([str(elem) for elem in pl2])
    if playDict.get(playStr,-1)==0:
        pl1.append(pl1[0])
        pl1.append(pl2[0])
        pl1.pop(0)
        pl2.pop(0)
    else:
        playDict.update({playStr:0})
        while len(pl1)!=0 and len(pl2)!=0:
            i+=1
            #print(i,pl1,pl2)
            if (len(pl1)-1)>=pl1[0] and (len(pl2)-1)>=pl2[0]:
                #print("rec!")
                tmp1,tmp2=playGame(pl1[1:pl1[0]],pl2[1:pl2[0]])
                if len(tmp1)!=0:
                    pl1.append(pl1[0])
                    pl1.append(pl2[0])
                else:
                    pl2.append(pl2[0])
                    pl2.append(pl1[0])
            elif pl1[0]>pl2[0]:
                pl1.append(pl1[0])
                pl1.append(pl2[0])
            else:
                pl2.append(pl2[0])
                pl2.append(pl1[0])
            pl1.pop(0)
            pl2.pop(0)
            #print(pl1,pl2)
    return (pl1,pl2)

out1,out2=playGame(sub1,sub2)

if len(out1)!=0:
    pl=out1
else:
    pl=out2

i=1
sum=0

for x in list(reversed(pl)):
    sum=sum+x*i
    i=i+1

print(sum)