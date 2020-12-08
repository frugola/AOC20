import re
from copy import deepcopy

class HandHeld:

    # state is the accumulator (state of the machine), int
    # prog is the program to be executed, list
    # pter is the pointer to NEXT instruction to be executed, int
    # the cmd in prog is a list of 2 fields: one is text one is signed integer

    def __init__(self):
        self.state = 0
        self.prog = []
        self.pter = 0
    
    def set_state(self,val): # sets the value of the state
        self.state = val

    def set_prog(self,commds): # feeds a program
        self.prog = commds
    
    def set_pter(self,val): # sets the pointer
        self.pter = val

    def step(self):
        if self.pter == len(self.prog): 
            print("Program Ended")
        else :
            cmd = self.prog[self.pter]
            #print("BEFORE cmd \n", self.state, "\n",self.prog,"\n",self.pter)
            if cmd[0]=="nop" : self.pter += 1
            elif cmd[0]=="acc" : self.__acc(cmd[1])
            elif cmd[0]=="jmp" : self.__jmp(cmd[1])
            #print("AFTER cmd \n", self.state, "\n",self.prog,"\n",self.pter)

    def run(self):
        while True:
            if self.pter == len(self.prog):
                print("Program Ended")
                break
            elif self.pter > len(self.prog):
                print("Program Aborted")
                break
            else : self.step() 

    # private methods
    
    def __acc(self,val):
        self.state += val
        self.pter += 1
    
    def __jmp(self,val):
        self.pter += val




def test_hh():
    hh = HandHeld()
    hh.set_prog([["acc",3],["acc",-1]])
    hh.run()
    print(hh.state)
    print(hh.pter)

#test_hh()



program = []
in_f = open("day_08_input")
for line in in_f:
    cmd = line[0:3]
    val = re.findall("\d+",line)[0]
    if line[4] == "+": 
        val = int(val)
    else :
        val = -int(val)
    program += [[cmd,val]]


def star_1(program):
    hh = HandHeld()
    hh.set_prog(program)
    visited = []
    while True:
        if hh.pter not in visited:
            visited += [hh.pter]
            hh.step()
        else:
            print(hh.state)
            break


def is_loopy(program):
    hh = HandHeld()
    hh.set_prog(program)
    visited = []
    flag = False
    while flag == False:
        if hh.pter not in visited and hh.pter < len(program):
            visited+=[hh.pter]
            hh.step()
        elif hh.pter in visited:
            flag = True
        elif hh.pter == len(program):
            break
    return flag
        

def star_2(program):
    for idx,cmd in enumerate(program):
        pgm = deepcopy(program) # modify this to deep copy
        if cmd[0]=="nop" : 
            pgm[idx][0] = "jmp"
        elif cmd[0]=="jmp" : 
            pgm[idx][0] = "nop"
        else : pass
        if is_loopy(pgm) == False:
            break

    hh = HandHeld()
    hh.set_prog(pgm)
    hh.run()
    print(hh.state)
        


star_1(program)
star_2(program)

