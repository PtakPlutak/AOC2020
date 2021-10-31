f = open("input.txt", "r")
inp=f.readlines()
f.close()

# while line!="\n":
#     for line in inp:
#         print(line)
import re
#line="departure location: 34-724 or 735-974"
#line=line.split(": ").split("-").split(" or ")
#line=re.split(": |-| or ",line)
mrng=[]

i=0
while inp[i]!="\n":
    line=re.split(": |-| or ",inp[i])
    mrng.extend(range(int(line[1]),int(line[2])+1))
    mrng.extend(range(int(line[3]),int(line[4])+1))
    i+=1
i=i+5
sum=0
for k in range(i,len(inp)):
    line=inp[k].strip().split(",")
    for v in line:
        if int(v) not in mrng:
            print(v)
            sum=sum+int(v)

print(sum)
# rng=[]
# rng.extend(range(2,5))
# rng.extend(range(10,12))
# i=724
# if i in rng:
#     print("yes")
# else:
#     print("no")

