import re
from itertools import product
from collections import Counter
from termgraph.termgraph import chart


# i.e 1d4+2d4+1+-1
def validInput(inp: str) -> bool:
    li = inp.split('+')
    for i in li:
        if bool(re.match(r'^-[0-9]+d[0-9]+$|^[0-9]+d[0-9]+$|^-[0-9]+$|^[0-9]+$',i)) == False:
            return False
    return True

def modToDice(inp: str) -> list:
    li = inp.split('+')
    dicedmod=[]
    for i in li:
        if bool(re.match(r'^-[0-9]+d[0-9]+$|^[0-9]+d[0-9]+$',i)) == False:
            if i[0] == '-':
                dicedmod.append(f'{i}d1')
            else:
                dicedmod.append(f'{i}d1')
        else:
            dicedmod.append(i)
    return dicedmod

# ['2d4','1d8','8d1']
def separateDice(inp: str) -> list:
    dicedmod = modToDice(inp)
    finalDiceList=[]
    for i in dicedmod:
        if i[0] == '-':
            for _ in range(int(i[1:i.index('d')])):
                finalDiceList.append(f'-1{i[i.index("d"):]}')
        else:
            for _ in range(int(i[0:i.index('d')])):
                finalDiceList.append(f'1{i[i.index("d"):]}')
    return finalDiceList

def stats(inp: str, termgraph_args: dict):
    finalDice = separateDice(inp)
    finalList=[]
    for i in finalDice:
        li=[]
        if i[0] == '-':
            for j in range(int(f'-{i[3:]}'),0):
                li.append(j)
        else:
            for k in range(1,int(i[2:])+1):
                li.append(k)
        finalList.append(li)
    dice_combination = product(*finalList)
    space = list(map(sum,dice_combination))
    space.sort()
    print()
    print(f'min: {space[0]}')
    print(f'max: {space[-1]}')
    print(f'average: {sum(space)/len(space)}')
    print()
    freqs = Counter(space)
    labels = list(map(str,list(freqs.keys())))
    data = []
    for i in list(freqs.values()):
        dataco=[]
        dataco.append(i)
        data.append(dataco)

    chart(colors=[],args=termgraph_args,labels=labels,data=data)
