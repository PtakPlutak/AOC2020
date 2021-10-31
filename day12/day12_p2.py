f = open("input.txt", "r")
inp=f.readlines()
f.close()

x=10
y=1
xs=0
ys=0
dir="E"
dirs=("E","S","W","N")
#how=inp[0]
#print(int(how[1:]))

def move(how):
    global x
    global y
    if how[0]=="E":
        x=x+int(how[1:])
    elif how[0]=="W":
        x=x-int(how[1:])
    elif how[0]=="N":
        y=y+int(how[1:])
    elif how[0]=="S":
        y=y-int(how[1:])
        
def updir(how):
    global x
    global y
    rnd=int(how[1:])
    tmpx=x
    tmpy=y
    if how[0]=="L":
        rnd=(rnd+180)%360
        #print(rnd)
    if rnd==90:
        x=tmpy
        y=-tmpx
    elif rnd==180 or rnd==0:
        x=-tmpx
        y=-tmpy
    elif rnd==270:
        x=-tmpy
        y=tmpx

for line in inp:
    if line[0]=="R" or line[0]=="L":
        updir(line)
    elif line[0]=="F":
        #move(dir+line[1:])
        xs=xs+x*int(line[1:])
        ys=ys+y*int(line[1:])
    else:
        move(line)
    
print(xs,ys,abs(xs)+abs(ys))