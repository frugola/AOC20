import numpy as np
import re
from copy import deepcopy

def parse(filename,star):
    start = []
    cube = {}
    in_f = open(filename,"r")
    for line in in_f:
        line = line.strip("\n\n")
        start+=[line]
    in_f.close()
    size = len(start[0])
    if star==1:
        for x in range(0,size):
            for y in range(0,size):
                if start[x][y]==".":cube[(0,x,y)] = 0
                elif start[x][y]=="#":cube[(0,x,y)]=1
    elif star==2:
        for x in range(0,size):
            for y in range(0,size):
                if start[x][y]==".":cube[(0,0,x,y)] = 0
                elif start[x][y]=="#":cube[(0,0,x,y)]=1
    return cube

def expand(cube):
    dims = len(list(cube.keys())[0])
    maxs = [0 for i in range(0,dims)]
    mins = [0 for i in range(0,dims)]
    for idx,el in enumerate(cube):
        for coord,coord_value in enumerate(el):
            if coord_value > maxs[coord] : maxs[coord]=coord_value
            if coord_value < mins[coord] : mins[coord]=coord_value
    if dims == 3:
        for s in range(mins[0]-1,maxs[0]+2):
            for r in range(mins[1]-1,maxs[1]+2):
                for c in range(mins[2]-1,maxs[2]+2):
                    if (s,r,c) not in cube: cube[(s,r,c)]=0
    elif dims == 4:
        for n in range(mins[0]-1,maxs[0]+2):
            for s in range(mins[1]-1,maxs[1]+2):
                for r in range(mins[2]-1,maxs[2]+2):
                    for c in range(mins[3]-1,maxs[3]+2):
                        if (n,s,r,c) not in cube: cube[(n,s,r,c)]=0

    return cube


def neighborhood(cube,coord):
    acc = 0
    dims = len(list(cube.keys())[0])
    if dims == 3 : 
        slixe,row,col = coord
        for s in range(slixe-1,slixe+2):
            for r in range(row-1,row+2):
                for c in range(col-1,col+2):
                    if (s,r,c) in cube: acc += cube[(s,r,c)]
    elif dims == 4:
        newt,slixe,row,col = coord
        for n in range(newt-1,newt+2):
            for s in range(slixe-1,slixe+2):
                for r in range(row-1,row+2):
                    for c in range(col-1,col+2):
                        if (n,s,r,c) in cube: acc += cube[(n,s,r,c)]
    return acc - cube[coord]


def update(cube):
    cube = expand(cube)
    new_cube = deepcopy(cube)
    for idx,coord in enumerate(cube):
        neigh = neighborhood(cube,coord)
        if cube[coord] == 1 and neigh in [2,3]:pass
        elif cube[coord] ==1 :
            new_cube[coord] = 0
        if cube[coord] == 0 and neigh == 3: new_cube[coord] = 1
    return new_cube


def star_1(cube,iters):
    for ii in range(0,iters):
        print(ii)
        cube = update(cube)
    actives = 0
    for idx,key in enumerate(cube):
        actives += cube[key]
    print(actives)


        
start_1 = parse("day_17_input",1)
start_2 = parse("day_17_input",2)
t1 = parse("test",1)
t2 = parse("test",2)

star_1(start_1,6)
star_1(start_2,6)


