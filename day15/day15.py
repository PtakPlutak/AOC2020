# f = open("input.txt", "r")
# inp=f.readlines()
# f.close()

inp=[0,3,6]
inp=[3,1,2]
inp=[2,15,0,9,1,20]

#inp.append(0)
#print(len(inp))
#print(inp.count(0))
for x in range(len(inp),2020):
    #print(x,inp[x-1])
    if inp[:-1].count(inp[x-1])==0:
        inp.append(0)
    else:
        indices = [i for i, y in enumerate(inp) if y == inp[x-1]]
        inp.append(indices[-1]-indices[-2])

print(inp[-1])
