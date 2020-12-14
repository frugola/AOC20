from numpy import binary_repr
import re

prog = []
in_f = open("day_14_input","r")
prog = [line.split(" = ") for line in in_f]
prog = [[line[0],line[1].rstrip()] for line in prog]


def init(prog):
    stack = {}
    mask = ""
    for item in prog:
        if item[0] == "mask": mask=item[1]
        else:
            mem = int(re.findall("\d+",item[0])[0])
            val = int(item[1])
            val_bin = binary_repr(val,width=36)
            for idx,bit in enumerate(val_bin):
                if mask[idx] == "X": pass
                elif mask[idx] == "1" : val_bin=val_bin[0:idx]+"1"+val_bin[idx+1:]
                elif mask[idx] == "0" : val_bin=val_bin[0:idx]+"0"+val_bin[idx+1:]
            stack[mem] = val_bin
    return stack


def address_dec(prog):
    stack = {}
    mask = ""
    for item in prog:
        if item[0] == "mask":mask=item[1]
        else:
            mem_bin = binary_repr(int(re.findall("\d+",item[0])[0]),width=36)
            val = int(item[1])
            for idx,bit in enumerate(mem_bin):
                if mask[idx] == "1": mem_bin=mem_bin[0:idx]+"1"+mem_bin[idx+1:]
                elif mask[idx]=="0": pass
                elif mask[idx]=="X": mem_bin=mem_bin[0:idx]+"X"+mem_bin[idx+1:]
            idxs = [idx for idx,bit in enumerate(mem_bin) if bit=="X"]
            combos = [binary_repr(i,width=len(idxs)) for i in range(0,2**len(idxs))]
            for cc in combos:
                list_mem_bin = [i for i in mem_bin]
                for ii,bb in enumerate(cc):
                    list_mem_bin[idxs[ii]] = bb
                updated_mem_bin = "".join(list_mem_bin)
                stack[int(updated_mem_bin,2)] = val
    return stack
        



def star_1(prog):
    acc = 0
    stack = init(prog)
    for item in stack: 
        acc += int(stack[item],2)
    print(acc)

def star_2(prog):
    acc = 0
    stack = address_dec(prog)
    for item in stack: 
        acc += stack[item]
    print(acc)

star_1(prog)
star_2(prog)

