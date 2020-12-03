import re

in_f = open("day_03_input","r")
f_map = in_f.readlines()
in_f.close()

f_mapp =[] # remove trailing 
for line in f_map:
    f_mapp += [re.sub("\s","",line)]

def move_by(mapp,moves): # moves are nb of steps: moves = [up,down,left,right]
    trees = 0
    width = len(mapp[0])
    height = len(mapp)
    row,col = 0,0
    while row < height:
        if (row + (moves[1]-moves[0])) < height : 
            row += (moves[1]-moves[0])
        else :
            return trees 
            break
        col = (col + (moves[3]-moves[2])) % width
        if mapp[row][col] == "#" : trees += 1
    return trees

def star_1(f_mapp):
    print(move_by(f_mapp,[0,1,0,3]))


def star_2(f_mapp):
    print(move_by(f_mapp,[0,1,0,1])*move_by(f_mapp,[0,1,0,3])*move_by(f_mapp,[0,1,0,5])*move_by(f_mapp,[0,1,0,7])*move_by(f_mapp,[0,2,0,1]))


star_1(f_mapp)
star_2(f_mapp)




