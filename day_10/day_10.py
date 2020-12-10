from copy import deepcopy

in_f = open("day_10_input","r")
adapt = [int(line.strip("\n")) for line in in_f]
in_f.close()

test_1 = [16,10,15,5,1,11,7,19,6,12,4]

test_2 =[28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]


def star_1(a):
    adapt = deepcopy(a) 
    jolt = 0
    diff = 1
    diff_1 = 0
    diff_3 = 0
    while sum(adapt)>0:
        jolt += 1
        if jolt in adapt:
            if diff == 1 :diff_1 += 1
            elif diff == 3 : diff_3 += 1
            diff = 1 
            idx = adapt.index(jolt)
            adapt[idx] = 0
        else : diff += 1
    return diff_1*(diff_3+1)


def choices(intv):
    if len(intv)<= 2 : return 1
    elif len(intv) == 3 : return 2
    elif len(intv) == 4 : return 4
    elif len(intv) == 5 : return 7 


def star_2(adapt):
    buckets = []
    adapt = sorted(adapt)
    adapt = [0] + sorted(adapt) + [adapt[-1]+3]
    root_idx = 0
    for a in adapt[:-1]:
        if not (a+1 in adapt or a+2 in adapt):
            idx = adapt.index(a+3) # mandatory point
            buckets += [adapt[root_idx:idx]] # start and end are mandatory points
            root_idx = idx
    acc = 1
    for b in buckets:
        acc = acc*choices(b)
    print(acc)
    #print([len(item) for item in buckets ])
    #print(buckets)


print(star_1(adapt))
star_2(adapt)






