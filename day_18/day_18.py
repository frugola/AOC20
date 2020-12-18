import re

in_f = open("day_18_input","r")
dump = in_f.readlines()
in_f.close()

test = dump[0].strip("\n")

def sub_eval(exp):
    # evaluates expression without parenthesis in order
    val = int(re.search("\d+",exp).group())
    exp = exp.split(" ")
    exp = " ".join(exp[1:])
    while re.search("\d+",exp)!=None:
        op = re.search("\+|\*",exp).group()
        val_1 = int(re.search("\d+",exp).group())
        if op == "+" : val += val_1
        elif op == "*":val = val*val_1
        exp = exp.split(" ")
        exp = " ".join(exp[2:])
    return val

def eval(exp,star):
    if star == 1: return sub_eval(exp)
    elif star == 2:
        exp = exp.split(" * ")
        for idx,item in enumerate(exp):
            addends =  item.split(" + ")
            acc = 0
            for a in addends: acc+=int(a)
            exp[idx] = acc
        prod = 1
        for item in exp: prod=prod*int(item)
        return prod


def get_par(exp):
    # get the content of a parenthesis
    e1 = exp
    while re.search("\(",e1[1:]) != None:
        e1 = re.search("\(.+",e1[1:]).group()
    while re.search("\)",e1[:]) != None:
        e1 = re.search(".+\)",e1).group()
        e1 = e1[:-1]
    return e1[1:]

def simplify(line,star):
    tmp = line
    # find the innermost parenthesis in tmp
    while "(" and ")" in tmp:
        tmp = get_par(tmp)
    # find the value of the innermost p.
    val = eval(tmp,star)
    # substitute the parenthesis
    tmp = [ii for ii in tmp]
    for idx,el in enumerate(tmp):
        if el=="+":tmp[idx]="\+"
        elif el=="*":tmp[idx]="\*"
    tmp = "".join(tmp)
    tmp = "".join(["\(",tmp,"\)"])
    return re.sub(tmp,str(val),line)

def eval_line(line,star):
    while "(" in line and ")" in line:
        line = simplify(line,star)
    return eval(line,star)

def star(dump,star):
    acc = 0
    for line in dump:
        line = line.strip("\n")
        acc+=eval_line(line,star)
    print(acc)

#star(dump,1)
star(dump,2)







 
