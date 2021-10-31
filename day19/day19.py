f = open("input_t.txt", "r")
inp=f.readlines()
f.close()

line=inp[0]
i=1
ruld={}
while ":" in line:
    line=line.split(":")
    ruld.update({int(line[0]):line[1][1:-1]})
    i=i+1
    line=inp[i]
    
stRule=inp[0].split(":")[1][1:-1]
resd={strule:1}

def istnum(s):
    return any(i.isdigit() for i in s)

sumk=1
while sumk!=0:
    sumk=0
    tmpresd=resd
    for k in resd.keys():
        if istnum(k):
            sumk+=1
            k=k.split(" ")
            for s in k:
                if istnum(s):
                    tmp=ruld[int(s)]
                    if "|" in tmp:
                        tmp=tmp.split(" | ")
                        
                    else
                        