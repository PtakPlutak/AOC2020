f = open("input.txt", "r")
inp=f.readlines()
f.close()
inp2=inp
inp3=inp
print(len(inp))
print(len(inp2))
print(len(inp3))

for x in inp:
    for y in inp2:
        for z in inp3:
            if int(x)+int(y)+int(z) == 2020:
                print(x,y,z,int(x)*int(y)*int(z))
