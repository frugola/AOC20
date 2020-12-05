import re
import math
import numpy as np

test = "FFBBBFBLRL"

def get_interval(letter,interval):
    if letter == "F" or letter == "L": 
        return [interval[0],interval[1]-math.ceil(interval[1]/2-interval[0]/2)]
    if letter == "B" or letter == "R": 
        return [interval[0]+math.ceil(interval[1]/2-interval[0]/2),interval[1]]

def get_seat(bpass):
    interval = [0,127]
    for ii in range(0,7):
        interval = get_interval(bpass[ii],interval)
        if interval[0]==interval[1] : row = interval[0]
    interval = [0,7]
    for ii in range(7,10):
        interval = get_interval(bpass[ii],interval)
        if interval[0]==interval[1] : col = interval[0]
    return [row,col]

def get_seat_id(seat):
    return 8*seat[0] + seat[1]

def star_1():
    hi_val = 0
    in_f = open("day_05_input")
    for bpass in in_f:
        bpass  = re.sub("\s","",bpass)
        val = get_seat_id(get_seat(bpass))
        if val > hi_val : hi_val = val
    in_f.close()
    return hi_val


def get_cabin():
    cabin = np.zeros((128,8))
    in_f = open("day_05_input")
    for bpass in in_f:
        bpass = re.sub("\s","",bpass)
        seat = get_seat(bpass)
        cabin[seat[0],seat[1]] = 1
    front_rows = 0
    while sum(cabin[0,:]==0):
        cabin = cabin[1:,:]
        front_rows += 1
    while sum(cabin[-1,:]==0): cabin = cabin[:-1,:]
    return cabin,front_rows


def star_2():
    cabin,front_offset = get_cabin()
    for ii in range(0,cabin.shape[0]):
        if sum(cabin[ii,:]) == 7:
            row_tmp = ii
            for kk in range(0,8):
                if cabin[ii,kk]==0: col = kk
            break
    row = row_tmp + front_offset
    return(get_seat_id([row,col]))
    


# print(get_seat(test))
#print(star_1())
print(star_2())
    
