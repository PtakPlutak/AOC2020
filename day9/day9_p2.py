f = open("input.txt", "r")
inp=f.readlines()
f.close()
inp2=[]
for i in inp:
    inp2.append(int(i))

goal=248131121
#goal=127

for ind in range(len(inp2)):
    i=1
    while sum(inp2[ind:ind+i])<goal:
        i+=1
    if sum(inp2[ind:ind+i])==goal:
        print(ind,ind+i,inp2[ind],inp2[ind+i-1],(inp2[ind]+inp2[ind+i-1]),sum(inp2[ind:ind+i]))
        print(min(inp2[ind:ind+i]), max(inp2[ind:ind+i]))
        print(min(inp2[ind:ind+i])+max(inp2[ind:ind+i]))