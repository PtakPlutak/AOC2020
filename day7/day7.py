f = open("input.txt", "r")
inp=f.readlines()
f.close()

checkL=[0]*len(inp)

def checkLine(bColour):
    for ind, line in enumerate(inp):
        if (" "+bColour) in line:
            checkL[ind]+=1
            checkLine(line.split(" ")[0] + " " + line.split(" ")[1]) 


checkLine("shiny gold")

sumM=0
for v in checkL:
    if v!=0:
        sumM+=1

print(sumM)