import re

def star_1():
    valid = 0
    in_f = open("day_02_input","r")
    for line in in_f:
        pswd = re.split("\s",line)
        [lo,hi] = [int(item) for item in re.split("-",pswd[0])]
        if (pswd[2].count(pswd[1][0]) <= hi) and (pswd[2].count(pswd[1][0]) >= lo):
            valid += 1
    
    in_f.close()
    return(valid)


def star_2():
    valid = 0
    in_f = open("day_02_input","r")
    for line in in_f:
        pswd = re.split("\s",line)
        [x,y] = [int(item) for item in re.split("-",pswd[0])]
        if (pswd[2][x-1] == pswd[1][0]) != (pswd[2][y-1] == pswd[1][0]):
            valid += 1
    in_f.close()
    return(valid)


print(star_1())
print(star_2())
