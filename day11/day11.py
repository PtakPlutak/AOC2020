f = open("input_t.txt", "r")
inp=f.readlines()
f.close()
sumx=0
inp2=[]
inp2.append(list("."*(len(inp[0])+1)))
for line in inp:
    inp2.append(list("."+line.replace("\n",".")))
inp2.append(list("."*(len(inp[0])+1)))


def updateMat(mat1):
    mat2=mat1
    for idx in enumerate(mat1):
        for idy, val in enumerate(line):
            if val=="#":
                if mat1[idx-1:idx+1][idy-1:idy+1].count("#")>5:
                    mat2[idx][idy]="L"
            elif val=="L":
                if mat1[idx-1:idx+1][idy-1:idy+1].count("#")==0:
                    mat2[idx][idy]="#"
    return mat2
initmat=inp2
tempmat=updateMat(initmat)
tempmat=updateMat(tempmat)
for x in initmat:
    print(x)

for x in tempmat:
    print(x)
# while initmat!=tempmat:
#     initmat=tempmat
#     tempmat=updateMat(initmat)
# 
# sumx=0
# for li in tempmat:
#     for x in li:
#         if x=="#": sumx+=1
#         
# print(sumx)
