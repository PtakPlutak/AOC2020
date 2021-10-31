f = open("input.txt", "r")
inp=f.readlines()
f.close()

x=0
y=0
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
    global dir
    rnd=int(int(how[1:])/90)
    curdir=dirs.index(dir)
    if how[0]=="R":
        dir=dirs[(curdir+rnd)%4]
    else:
        #print(rnd, curdir, rnd-curdir+4,(rnd-curdir+4)%4)
        dir=dirs[(curdir-rnd+4)%4]

for line in inp:
    if line[0]=="R" or line[0]=="L":
        updir(line)
    elif line[0]=="F":
        move(dir+line[1:])
    else:
        move(line)
    
print(x,y,abs(x)+abs(y))