import string

alpha="abcdefghijklmnopqrstuvwxyza"
code="eqbpntwemza"

for i in range(26):
    str=""
    for j in range(len(code)):
        str+=alpha[alpha.find(code[j])+1]
    print str
    code=str