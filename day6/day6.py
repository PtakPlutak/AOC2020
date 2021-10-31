def checkLine(line):
    alf=set("qwertyuiopasdfghjklzxcvbnm")
    retVal=len(alf.intersection(line))
    return retVal

f = open("input.txt", "r")
inp=f.readlines()
f.close()

sumP=0
lineS=""

for lineX in inp:
    if lineX.isspace():
        #print(lineS)
        #print(checkLine(lineS))
        sumP=sumP+checkLine(lineS)
        lineS=""
    else:
        lineS=lineS + lineX

#print(checkLine(lineS))
sumP=sumP+checkLine(lineS)
            
print(sumP)