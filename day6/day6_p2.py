def checkLine(line):
    m=line.split("\n")
    #print(m,"tu5")
    tset=set(m[0])
    #print(tset,"tu4")
    for mp in m:
        #print(mp,"tu")
        if mp != "":
            tset=tset.intersection(set(mp))
    #print(tset,"tu2")
    retVal=len(tset)
    return retVal

f = open("input.txt", "r")
inp=f.readlines()
f.close()

sumP=0
lineS=""

for lineX in inp:
    if lineX.isspace():
        #print(lineS)
        print(checkLine(lineS),"tu3")
        sumP=sumP+checkLine(lineS)
        lineS=""
    else:
        lineS=lineS + lineX

print(checkLine(lineS),"tu3")
sumP=sumP+checkLine(lineS)

            
print(sumP)