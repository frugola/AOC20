import numpy as np
import re

param = 10000

def get_seat_map(list_chars):
    s_map = []
    for item in list_chars:
        item = [l for l in item[0:-1]]
        for idx,letter in enumerate(item):
             if letter == "L" : item[idx]  = 0
             elif letter == ".": item[idx] = param
             elif letter == "#": item[idx] = 1
        s_map += [item]
    return np.asarray(s_map)

str_seats = []
in_f = open("day_11_input","r")
str_seats = in_f.readlines()
seats = get_seat_map(str_seats)

str_test_1=["L.LL.LL.LL\n","LLLLLLL.LL\n","L.L.L..L..\n","LLLL.LL.LL\n","L.LL.LL.LL\n","L.LLLLL.LL\n","..L.L.....\n","LLLLLLLLLL\n","L.LLLLLL.L\n","L.LLLLL.LL\n"]
test_1 = get_seat_map(str_test_1)


def neighborhood(s_map,r,c,star):
    rows,cols = s_map.shape
    val = s_map[r,c]
    if star==1 and (r == 0 or c == 0 or r==rows-1 or c==cols-1):
        # zero padding all around
        s_map = np.vstack((np.zeros(cols),s_map))
        s_map = np.vstack((s_map,np.zeros(cols)))
        s_map = np.hstack((np.zeros((rows+2,1)),s_map))
        s_map = np.hstack((s_map,np.zeros((rows+2,1))))
        r = r+1
        c = c+1
    if star==1:
        target= s_map[r-1:r+2,c-1:c+2]
        return (sum(sum(target))%10-val)
    elif star==2:
        acc = 0
        # sum horizontal
        i = 1
        while (c+i)< cols:
            if s_map[r,c+i] == 1: 
                acc+=1
                break
            elif s_map[r,c+1] == 0: break
            i+=1
        i=1
        while c-i >= 0:
            if s_map[r,c-i] == 1:
                acc+=1
                break
            elif s_map[r,c-i] == 0: break
            i+=1
        #print("horiz",acc)
        # sum vertical
        i=1
        while (r+i) < rows:
            #print([r+i],s_map[r+i,c])
            if s_map[r+i,c] == 1:
                acc+=1
                break
            elif s_map[r+i,c] == 0 : break
            i+=1
        i=1
        while r-i >= 0:  
            #print([r-i],s_map[r-i])
            if s_map[r-i,c] == 1:
                acc += 1
                break
            elif s_map[r-i,c] == 0: break
            i+=1
        #print("vert",acc)
        # first diagonal
        i=1
        while (r+i)<rows and (c+i)<cols:
            #print([r+i,c+i],s_map[r+i,c+i])
            if s_map[r+i,c+i] == 1:
                acc+=1
                break
            elif s_map[r+i,c+i] == 0: break
            i += 1
        i=1
        while (r-i)>=0 and (c-i)>=0:
            #print(" here" )
            #print([r-i,c-i],s_map[r-i,c-i])
            if s_map[r-i,c-i] == 1:
                acc+=1
                break
            elif s_map[r-i,c-i] == 0: break
            i += 1
        #print("diag1",acc)
        # second diagonal
        i=1
        while (r+i)<rows and (c-i)>=0: 
            #print([r+i,c-i],s_map[r+i,c-i])
            if s_map[r+i,c-i] == 1:
                acc += 1
                break
            elif s_map[r+i,c-i] == 0: break
            i += 1
        i=1
        while r-i>=0 and c+i<cols: 
            if s_map[r-i,c+i] == 1:
                acc +=1
                break
            elif s_map[r-i,c+i] == 0: break
            i +=1
        #print("diag2",acc)
        return acc%param


def update_seats(s_map,star):
    rows,cols = s_map.shape
    new_map = np.zeros((rows,cols))
    for r in range(0,rows):
        for c in range(0,cols):
            if star == 1:
                if s_map[r,c]==0 and neighborhood(s_map,r,c,star)==0:new_map[r,c]=1
                elif s_map[r,c]==1 and neighborhood(s_map,r,c,star)>=4:new_map[r,c]=0
                else: new_map[r,c] = s_map[r,c]
            elif star == 2:
                #print(neighborhood(s_map,r,c,star))
                if s_map[r,c]==0 and neighborhood(s_map,r,c,star)==0:new_map[r,c]=1
                elif s_map[r,c]==1 and neighborhood(s_map,r,c,star)>=5:new_map[r,c]=0
                else: new_map[r,c] = s_map[r,c]
    change_flag = not (sum(sum(new_map-s_map)) == 0)
    return (new_map,change_flag)


def star(s_map,star):
    change_flag = True
    ii = 0
    while change_flag == True:
        print(ii)
        s_map,change_flag = update_seats(s_map,star)
        ii+=1
    return(sum(sum(s_map))%param)


#print(star(seats,1))
print(star(seats,2))






