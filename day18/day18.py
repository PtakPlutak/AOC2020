inp="5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"

def evalExp(inexp):
    inexp=inexp.split(" ")
    while len(inexp)!=1:
        inexp[0]=eval(str(inexp[0])+inexp[1]+inexp[2])
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