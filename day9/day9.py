f = open("input.txt", "r")
inp=f.readlines()
f.close()
inp2=[]
for i in inp:
    inp2.append(int(i))

def checkList(k, sum):
    k2=k
    #print(k,sum)
    for el1 in k:
        for el2 in k2:
            if el1+el2==sum:
                return 1
    return 0

prel=25
initv=0
for ind in range(prel,len(inp2)):
    if checkList(inp2[ind-prel:ind],inp2[ind])==0:
        print(inp2[ind])
# k=inp2[initv:initv+prel]
# print(k)
# print(checkList(k,42))