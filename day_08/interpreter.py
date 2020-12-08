import re

class HandHeld:
    # state is the accumulator (state of the machine), int
    # prog is the program to be executed, list
    # pter is the pointer to NEXT instruction to be executed, int
    # the cmd in prog is a list of 2 fields: one is text one is signed integer
    def __init__(self):
        self.state = 0
        self.prog = []
        self.pter = 0
    
    # public methods

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


def load_prog(filename):
    # loads the program from a file 
    # where a line is an instruction
    program = []
    in_f = open(filename)
    for line in in_f:
        cmd = line[0:3]
        val = re.findall("\d+",line)[0]
        if line[4] == "+": 
            val = int(val)
        else :
            val = -int(val)
        program += [[cmd,val]]
    in_f.close()
    return program




    
