import re

# i.e 1d4+2d4+1+-1
def validInput(inp: str) -> bool:
    li = inp.split('+')
    for i in li:
        if bool(re.match(r'^-[1-9]+d[1-9]+$|^[1-9]+d[1-9]+$|^-[1-9]+$|^[1-9]+$',i)) == False:
            return False
    return True

def modToDice(inp: str) -> list:
    li = inp.split('+')
    dicedmod=[]
    for i in li:
        if bool(re.match(r'^[1-9]+d[1-9]+$|^[1-9]+d[1-9]+$',i)) == False:
            if i[0] == '-':
                dicedmod.append(f'-{i[1]}d1')
            else:
                dicedmod.append(f'{i[0]}d1')
        else:
            dicedmod.append(i)
    return dicedmod


