# f = open("input.txt", "r")
# inp=f.readlines()
# f.close()

inp=[0,3,6]
#inp=[3,1,2]
inp=[2,15,0,9,1,20]
memdict={}

for idx, val in enumerate(inp):
    memdict.update({val:idx})

for x in range(len(inp),30000000):
    #print(x,inp[x-1])
    if memdict.get(inp[x-1],-1)==-1:
        inp.append(0)
        memdict.update({inp[x-1]:(x-1)})
    else:
        #print(inp[x-1],inp[y],x,y)
        inp.append(x-1-memdict.get(inp[x-1]))
        memdict.update({inp[x-1]:(x-1)})

print(inp[-1])
