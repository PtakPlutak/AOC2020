def getVal(line):
    lineS=line.split(" ")
    return int(lineS[1])

def runProg(inp):
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
            break

f = open("input.txt", "r")
inp=f.readlines()
f.close()

indJ=[ind for ind, val in enumerate(inp) if "jmp" in val ]
indN=[ind for ind, val in enumerate(inp) if "nop" in val ]

for iJ in indJ:
    inp[iJ]=inp[iJ].replace("jmp","nop")
    runProg(inp)
    inp[iJ]=inp[iJ].replace("nop","jmp")


