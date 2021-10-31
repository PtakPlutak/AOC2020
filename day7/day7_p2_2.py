f = open("input.txt", "r")
inp=f.readlines()
f.close()

def checkLine(bColour):
    sumB=0
    for ind, line in enumerate(inp):
        if (bColour+ " bags contain") in line:
            lineS=line.split(" ")
            if lineS[4]=="no":
                pass
            else:
                i=4
                while i+3<len(lineS):
                    bag1C=int(lineS[i])
                    bag1N=lineS[i+1]+" "+lineS[i+2]
                    sumB=sumB+bag1C*(1+checkLine(bag1N))
                    i+=4

    return sumB   

print(checkLine("shiny gold"))