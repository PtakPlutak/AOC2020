def getVal(line):
    lineS=line.split(" ")
    return int(lineS[1])

f = open("input_t.txt", "r")
inp=f.readlines()
f.close()

insDict=set()
curPos=0
accu=0
#print(getVal("acc -4"))
while len(insDict.intersection(set([curPos])))==0:
    insDict.add(curPos)
    if inp[curPos][0]=="n":
        curPos+=1
    elif inp[curPos][0]=="a":
        accu=accu+getVal(inp[curPos])
        curPos+=1
    else: #jump
        curPos=curPos+getVal(inp[curPos])
    if curPos==len(inp):
        print(accu)
