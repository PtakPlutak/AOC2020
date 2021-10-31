def checkLine(line):
    retVal=0
    if (line.find("byr:") != -1):
        retVal+=1
    if (line.find("iyr:") != -1):
        retVal+=1
    if (line.find("eyr:") != -1):
        retVal+=1
    if (line.find("hgt:") != -1):
        retVal+=1
    if (line.find("hcl:") != -1):
        retVal+=1
    if (line.find("ecl:") != -1):
        retVal+=1
    if (line.find("pid:") != -1):
        retVal+=1
    return retVal

f = open("input.txt", "r")
inp=f.readlines()
f.close()

sumP=0
lineS=""

for lineX in inp:
    if lineX.isspace():
        #print(lineS)
        if checkLine(lineS)==7:
            sumP+=1
        lineS=""
    else:
        lineS=lineS + lineX

if checkLine(lineS)==7:
    sumP+=1
    lineS=""
            
print(sumP)


    