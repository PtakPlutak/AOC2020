f = open("input_t.txt", "r")
inp=f.readlines()
f.close()
#alle={}
alle=set()
foods={}

for line in inp:
    line_al=line.split("(contains")[1].replace(")","").strip().split(",")
    for al in line_al:
        alle.add(al.strip())

for line in inp:
    line_fd=line.split(" (contains")[0].split(" ")
    for fd in line_fd:
        foods.update({fd: als})
    
