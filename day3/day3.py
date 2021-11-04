f = open("input.txt", "r")
lines = f.readlines()
f.close()

print(len(lines),len(lines[0]))

#print(lines[0])
#print(lines[1])
#print(lines[0][0])
sumTrees=0
#print(lines[len(lines)-1])
#print(lines[0][3])
for x in range(len(lines)):
     #print(x,(3*x) % (len(lines[0])-1),lines[x][(3*x) % (len(lines[0])-1)])
     if lines[x][(3*x) % (len(lines[0])-1)]=="#":
#         #print("tree")
#         #lines[x][(3*x) % (len(lines[0])-1)]="X"
         sumTrees+=1
#     else:
#         #lines[x][(3*x) % (len(lines[0])-1)]="O"

#print(lines)
print(sumTrees)
