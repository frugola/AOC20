config = "198753462"
test = "389125467"

config_d ={}
for idx,item in enumerate(config):
    if idx < len(config)-1: 
        config_d[int(config[idx])] = int(config[idx+1])
    config_d[1000000]=int(config[0])
    config_d[int(config[-1])]=10

test_d ={}
for idx,item in enumerate(test):
    if idx < len(test)-1: 
        test_d[int(test[idx])] = int(test[idx+1])
    test_d[1000000]=int(test[0])
    test_d[int(test[-1])]=10


def round(cups,curr): # x is current cup
    print("cups: ",cups)
    print("curr: ", curr)
    base = len(cups)
    idx_curr = cups.index(curr)
    idx_move = [(idx_curr+i)%base for i in range(1,4)]
    move = [cups[ii] for ii in idx_move]
    print("pick up: ",move)
    if idx_move[0]==0:
        new = cups[3:]
    elif idx_move[0] < idx_move[-1]:
        new = cups[0:idx_move[0]] + cups[idx_move[-1]+1:]
    else:
        new = cups[idx_move[-1]+1:idx_move[0]]

    print("new ",new)
    dest = str(int(curr)-1)
    if dest == "0": dest = "9"
    while dest in move:
        if int(dest) > 1: dest = str(int(dest)-1)
        else : dest = "9"
    print("destination: ",dest)
    idx_dest = new.index(dest)
    new = new[0:idx_dest+1] + "".join(move) + new[idx_dest+1:]
    print(new)
    print("\n")
    return new,new[(new.index(curr)+1)%base]

def get_following(cups_d,item):
    if item in cups_d:return cups_d[item]
    else: return item +1

def get_dest(current,p1,p2,p3):
    not_set = [p1,p2,p3]
    candidate = current
    while True:
        candidate += -1
        if candidate == 0 : candidate = 1000000 
        if candidate not in not_set: break
    return candidate

def update(cups_d,current):
    p1 = get_following(cups_d,current)
    p2 = get_following(cups_d,p1)
    p3 = get_following(cups_d,p2)
    a = get_following(cups_d,p3)
    d = get_dest(current,p1,p2,p3)
    cups_d[current] = a
    cups_d[p3] = get_following(cups_d,d)
    cups_d[d] = p1
    return cups_d,get_following(cups_d,current)


def debug(test):
    curr = test[0]
    for ii in range(0,10):
        test,curr = round(test,curr)

def debug_d(test_d):
    current = 3
    for ii in range(0,10000000): 
        test_d,current=update(test_d,current)
    return test_d


def star_1(config):
    curr = config[0]
    for ii in range(0,100):
        config,curr = round(config,curr)

def star_2(config_d,config):
    current = int(config[0])
    for ii in range(0,10000000): 
        config_d,current=update(config_d,current)
    print(config_d[1]*config_d[config_d[1]])


