f = open("input.txt", "r")
inp=f.readlines()
f.close()

memdict={}

def upval(inval, ms):
    outval=""
    for i in range(36):
        if ms[i]=="X":
            outval=outval+inval[i]
        else:
            outval=outval+ms[i]
    return outval

mask=[]
for line in inp:
    if "mask" in line:
        mask=line[7:-1]
        #print(line,mask)
    else:
        loc=line.split("]")[0].split("[")[1]
        val=str(bin(int(line.split(" = ")[1].strip()))[2:]).zfill(36)
        memdict.update({loc: upval(val,mask)})
        #print(line.strip())
        #print(loc,val)
sumx=0
for x in memdict.values():
    #print(x,int(x,2))
    sumx+=int(x,2)
    
print(sumx)