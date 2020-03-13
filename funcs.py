import re
from itertools import product
from collections import Counter
from termgraph.termgraph import chart

termgraph_args = {'stacked':False,'width':50,'no_labels':False,
        'format':'{:<5.2f}','suffix':'','vertical':False
        }

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
        if bool(re.match(r'^-[1-9]+d[1-9]+$|^[1-9]+d[1-9]+$',i)) == False:
            if i[0] == '-':
                dicedmod.append(f'-{i[1]}d1')
            else:
                dicedmod.append(f'{i[0]}d1')
        else:
            dicedmod.append(i)
    return dicedmod

# ['2d4','1d8','8d1']
def separateDice(inp: str) -> list:
    dicedmod = modToDice(inp)
    finalDiceList=[]
    for i in dicedmod:
        if i[0] == '-':
            for _ in range(int(i[1])):
                finalDiceList.append(f'-1d{i[3]}')
        else:
            for _ in range(int(i[0])):
                finalDiceList.append(f'1d{i[2]}')
    return finalDiceList

def stats(inp: str):
    finalDice = separateDice(inp)
    finalList=[]
    for i in finalDice:
        li=[]
        if i[0] == '-':
            for j in range(int(f'-{i[3]}'),0):
                li.append(j)
        else:
            for k in range(1,int(i[2])+1):
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
