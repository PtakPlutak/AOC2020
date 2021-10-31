f = open("input_t.txt", "r")
inp=f.readlines()
f.close()
#alle={}
alle=set()
foods={}

for line in inp:
    line_al=line.split("(contains")[1].replace(")","").strip().split(",")
    line_fd=line.split(" (contains")[0].split(" ")
    for fd in line_fd:
        if fd in foods:
            aldict=foods[fd]
            aldict=foods[fd]
            aldict["all"]+=1
            for al in line_al:
                if al in aldict:
                    aldict[al.strip()]+=1
                else:
                    aldict[al.strip()]=1
            foods.update({fd: aldict})
        else:
            foods.update({fd: {}})
            aldict=foods[fd]
            aldict["all"]=1
            for al in line_al:
                aldict[al.strip()]=1
            foods.update({fd: aldict})
sum=0
for line in inp:
    line_al=line.split("(contains")[1].replace(")","").strip().split(",")
    line_fd=line.split(" (contains")[0].split(" ")
    for al in line_al:
        for fd in foods:
            aldict=foods[fd]
            if al.strip() in aldict and fd not in line:
                print(fd)
