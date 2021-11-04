f = open("input.txt", "r")
lines = f.readlines()
f.close()

sumTrees=0
multTrees=1

sls=[(1,1),(3,1),(5,1),(7,1),(1,2)]

#print(sls[1][0])

for slope in sls:
     #slope=(1,2)
     sumTrees=0
     for x in range(len(lines)):
         #print(x,x%slope[1],(slope[0]*x) % (len(lines[0])-1))
         if x % slope[1] == 0:
             #print(slope,x,slope[0]*x/slope[1])
             if lines[x][int((slope[0]*x/slope[1]) % 
(len(lines[0])-1))]=="#":
                 sumTrees+=1
     print(slope[0],slope[1],sumTrees)
     multTrees=multTrees*sumTrees

print(multTrees)

# for x in range(len(lines)):
#     #print(x,(3*x) % (len(lines[0])-1),lines[x][(3*x) % 
(len(lines[0])-1)])
#     if lines[x][(3*x) % (len(lines[0])-1)]=="#":
#         sumTrees+=1
#
#
# print(sumTrees)
