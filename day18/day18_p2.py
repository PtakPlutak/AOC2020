inp="((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

def evalExp(inexp):
    inexp=inexp.split(" ")
    while len(inexp)!=1:
        #pos=inexp.index("+") if "+" in inexp else -1
        while "+" in inexp:
            pos=inexp.index("+")
            inexp[pos]=str(eval(str(inexp[pos-1])+inexp[pos]+inexp[pos+1]))
            inexp.pop(pos+1)
            inexp.pop(pos-1)
        while "*" in inexp:
            inexp[0]=str(eval(inexp[0]+inexp[1]+inexp[2]))
            inexp.pop(1)
            inexp.pop(1)
    return str(inexp[0])

def remPar(inexp):
    start=inexp.rfind("(")
    stop=inexp.rfind("(")+inexp[inexp.rfind("("):].find(")")
    #print(inexp[start:stop])
    return (inexp[:start]+evalExp(inexp[start+1:stop])+inexp[stop+1:])

def calcExp(inexp):
    while inexp.find("(")!=-1:
        inexp=remPar(inexp)
    return evalExp(inexp)

#print(calcExp(inp))
f = open("input.txt", "r")
inp=f.readlines()
f.close()
sum=0
for line in inp:
    sum=sum+int(calcExp(line))
    
print(sum)