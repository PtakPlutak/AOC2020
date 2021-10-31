f = open("input.txt", "r")
inp=f.readlines()
f.close()
inp2=inp
inp3=inp
print(len(inp))
print(len(inp2))
print(len(inp3))
i=0
for x in inp:
    #print(x)
    for y in inp2:
        #print(x,y,x+y)
        if int(x)+int(y) == 2020:
            print(x,y,int(x)*int(y))

print(i)