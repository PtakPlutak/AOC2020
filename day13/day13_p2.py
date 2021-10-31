f = open("input.txt", "r")
inp=f.readlines()
f.close()
inp2=[]
inp3=[]

for id, i in enumerate(inp[1].split(",")):
    if i!="x":
        inp2.append(int(i))
        inp3.append(id)

def checkL(time):
    totval=0
    for id, val in enumerate(inp2):
        totval=totval+(time+inp3[id])%val
    return totval

#tim=int(100000000000000/inp2[0])*inp2[0]
tim=0
while checkL(tim)!=0:
    tim=tim+inp2[0]
    if tim>100000000000000: print(tim)
    if tim>10000000000000: print(tim)
    if tim>1000000000000: print(tim)
    if tim>100000000000: print(tim)
    if tim>10000000000: print(tim)
    if tim>1000000000: print(tim)
    if tim>100000000: print(tim)
    #if tim>10000000: print(tim)
    #if tim>1000000: print(tim)

print(tim)

# st=int(inp[0])
# #k=59
# #print(k-st%k)
# minVal=1000
# minValB=0
# for numB in inp2:
#     if numB>0:
#         if minVal>(numB-st%numB):
#             minVal=numB-st%numB
#             minValB=numB
# 
# print(minValB*minVal)