f = open("input.txt", "r")
inp=f.readlines()
f.close()

sumP=0

for lineX in inp:
    line=lineX.split()
    #print(line[1][0])
    #print(len(line[2])-len(line[2].replace(line[1][0],"")))
    lenRep=len(line[2])-len(line[2].replace(line[1][0],""))
    rng=line[0].split("-")
    if lenRep>=int(rng[0]) and lenRep<=int(rng[1]):
        sumP+=1

print(sumP)

# 
# for x in inp:
#     for y in inp2:
#         for z in inp3:
#             if int(x)+int(y)+int(z) == 2020:
#                 print(x,y,z,int(x)*int(y)*int(z))
