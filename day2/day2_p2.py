f = open("input.txt", "r")
inp=f.readlines()
f.close()

sumP=0

for lineX in inp:
    line=lineX.split()
    rng=line[0].split("-")
    if (line[2][int(rng[0])-1]==line[1][0]) != (line[2][int(rng[1])-1]==line[1][0]):
        sumP+=1

print(sumP)

# 
# for x in inp:
#     for y in inp2:
#         for z in inp3:
#             if int(x)+int(y)+int(z) == 2020:
#                 print(x,y,z,int(x)*int(y)*int(z))
