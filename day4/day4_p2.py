def checkLine(line):
    retVal=0
    #lineS=line.split()
    if (line.find("byr:") != -1):
        byr=int(line[line.find("byr:")+4:line.find("byr:")+8])
        #print(byr)
        if byr>1920 and byr<=2002:
            retVal+=1
    if (line.find("iyr:") != -1):
        iyr=int(line[line.find("iyr:")+4:line.find("iyr:")+8])
        print(iyr)
        if iyr>2010 and iyr<=2020:
            retVal+=1
    if (line.find("eyr:") != -1):
        iyr=int(line[line.find("iyr:")+4:line.find("iyr:")+8])
        print(iyr)
        if iyr>2010 and iyr<=2020:
            retVal+=1
    if (line.find("hgt:") != -1):
        hgtV=int(line[line.find("hgt:")+4:line.find("iyr:")+6])
        hgtU=line[line.find("hgt:")+7:line.find("iyr:")+8]
        print(hgtV,hgtU)
        if iyr>2010 and iyr<=2020:
            retVal+=1
    if (line.find("hcl:") != -1):
        retVal+=1
    if (line.find("ecl:") != -1):
        retVal+=1
    if (line.find("pid:") != -1):
        retVal+=1
    return retVal

f = open("input_p.txt", "r")
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


    