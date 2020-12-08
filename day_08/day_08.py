import re
from copy import deepcopy
from interpreter import HandHeld
from interpreter import load_prog


def test_hh():
    hh = HandHeld()
    hh.set_prog([["acc",3],["acc",-1]])
    hh.run()
    print(hh.state)
    print(hh.pter)

#test_hh()




def is_loopy(program):
    hh = HandHeld()
    hh.set_prog(program)
    visited = []
    flag = False
    while flag == False:
        if hh.pter not in visited and hh.pter < len(program):
            visited+=[hh.pter]
            hh.step()
        elif hh.pter in visited: flag = True
        elif hh.pter == len(program): break
    return flag,hh.state
        

def star_1(program):
    print(is_loopy(program)[1])

def star_2(program):
    for idx,cmd in enumerate(program):
        pgm = deepcopy(program) 
        if cmd[0]=="nop" : pgm[idx][0] = "jmp"
        elif cmd[0]=="jmp" : pgm[idx][0] = "nop"
        else : pass
        [flag,state] = is_loopy(pgm)
        if flag == False: 
            print(state)
            break


program = load_prog("day_08_input")

star_1(program)
star_2(program)

