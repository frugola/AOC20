in_f = open("day_12_input","r")
dirs = []
for line in in_f:
    line = line.strip()
    if line == "R270" : line = "L90"
    elif line == "L270" : line = "R90"
    elif line == "L180" : line = "R180" 
    dirs +=[[line[0],int(line[1:])]]

    
def go_left(h):
    if h=="N":h="W"
    elif h=="E":h="N"
    elif h=="S":h="E"
    elif h=="W":h="S"
    return h

def go_right(h,t): # t is either 90 or 180
    if h=="N" and t==90: h="E"
    elif h=="N" and t==180: h="S"
    elif h=="E" and t==90: h="S"
    elif h=="E" and t==180: h="W"
    elif h=="S" and t==90: h="W"
    elif h=="S" and t==180: h="N"
    elif h=="W" and t==90: h="N"
    elif h=="W" and t==180: h="E"
    return h

def move(h,s,instr):
    xi = None
    if instr[0]=="N" or instr[0]=="E" or instr[0]=="S" or instr[0]=="W":
        xi = instr[0]
    elif instr[0] == "F":
        xi = h
    elif instr[0] == "L": # always 90 degrees on the left
        h = go_left(h)
    elif instr[0] == "R":
        h = go_right(h,instr[1])
    
    if xi=="N" : s[0] += instr[1] 
    elif xi=="E" : s[1] += instr[1]
    elif xi=="S" : s[2] += instr[1]
    elif xi=="W" : s[3] += instr[1]
    return h,s

def get_manh(h,s,dirs): 
    # h is the heading
    # s is the state [n,e,s,w]
    # dirs is the list of instructions
    for instr in dirs:
        h,s = move(h,s,instr)
    return (abs(s[0]-s[2]) + abs(s[1]-s[3]))

#4 10 0 0 
#0 4 10 0
def way_right(w):
    w =[w[3]] + w[0:3]
    return w

def get_manh_way(h,w,s,dirs):
    # h is the heading
    # s is the state [n,e,s,w]
    # w is the waypoint [n,e,s,w]
    # dirs is the list of instructions
    for instr in dirs:
        times = 0
        if instr[0]=="N" or instr[0]=="E" or instr[0]=="S"or instr[0]=="W":
            h,w = move(h,w,instr)
        elif instr[0]=="F":
            update = [x*instr[1] for x in w]
            s = [s[i]+update[i] for i in range(0,len(s))]
        elif instr[0]=="R" and instr[1]==90:   times = 1
        elif instr[0]=="R" and instr[1]==180:times = 2
        elif instr[0]=="L" and instr[1]==90: times = 3
        for ii in range(0,times):
            w = way_right(w)
    return (abs(s[0]-s[2]) + abs(s[1]-s[3]))




test = [["F",10],["N",3],["F",7],["R",90],["F",11]]

def star_1():
    print(get_manh("E",[0,0,0,0],dirs))

def star_2():
    print(get_manh_way("E",[1,10,0,0],[0,0,0,0],dirs))


star_1()
star_2()
