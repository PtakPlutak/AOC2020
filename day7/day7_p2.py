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
            elif "," in line:
                bag1C=int(lineS[4])
                bag1N=lineS[5]+" "+lineS[6]
                bag2C=int(lineS[8])
                bag2N=lineS[9]+" "+lineS[10]
                sumB=sumB+bag1C*(1+checkLine(bag1N))+bag2C*(1+checkLine(bag2N))
                print(bag1C,"+",bag1C,"*",checkLine(bag1N),"+",bag2C,"+",bag2C,"*",checkLine(bag2N))
            else:
                bag1C=int(lineS[4])
                bag1N=lineS[5]+" "+lineS[6]
                sumB=sumB+bag1C*(1+checkLine(bag1N))
                print(bag1C,"+",bag1C,"*",checkLine(bag1N))
    return sumB   

print(checkLine("shiny gold"))