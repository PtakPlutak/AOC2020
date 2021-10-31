inexp="1 + 2 * (3 + 4) * (5 + 6)"


start=inexp.rfind("(")
stop=inexp.rfind("(")+inexp[inexp.rfind("("):].find(")")
print(inexp[start:stop])
print(inexp[:start])
print(inexp[stop+1:])
print(inexp[start+1:stop])
#return (inexp[:start]+evalExp(inexp[start+1:stop])+inexp[stop+1:])