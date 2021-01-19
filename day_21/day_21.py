import re
from copy import deepcopy

def parse_in(filename):
    in_f = open(filename,"r")
    ingredients = []
    allergens = []
    for line in in_f:
        line = re.sub("contains ","",line)
        line = re.sub("\)\n","",line)
        line = line.split(" (")
        ingredients += [line[0].split(" ")]
        allergens += [line[1].split(", ")]
    return ingredients, allergens

def candidate_allergen(ingredients,allergens,test_allergen):
    dump = []
    for idx,item in enumerate(ingredients):
        if test_allergen in allergens[idx]: dump += [item]
    candidates = []
    for elem in dump[0]:
        acc = 1
        for ii in range(1,len(dump)):
            if elem in dump[ii] : acc+=1
        if acc == len(dump): candidates+=[elem]
    return candidates

def compile_table(ingredients,allergens):
    all_table = {}
    candidates_table = {}
    for idx in range(0,len(ingredients)):
        for idy in range(0,len(allergens[idx])):
            if allergens[idx][idy] not in candidates_table:
                candidates_table[allergens[idx][idy]] = candidate_allergen(ingredients,allergens,allergens[idx][idy])
    return candidates_table

def parse_table(candidates_table):
    ones = []
    for idx,key in enumerate(candidates_table):
        if len(candidates_table[key])==1:
            ones += [key]
    for aller in ones:
        ing = candidates_table[aller][0]
        for idx,key in enumerate(candidates_table):
            if ing in candidates_table[key] and key != aller:
                candidates_table[key] = [item for item in candidates_table[key] if item != ing]
    return candidates_table


def star_1():
    ingredients,allergens = parse_in("day_21_input")
    allergen_table = compile_table(ingredients,allergens)
    for ii in range(0,10):
        allergen_table = parse_table(allergen_table)
    danger = [allergen_table[key][0] for idx,key in enumerate(allergen_table)]
    acc = 0
    for elem in ingredients:
        for idx in elem:
            if idx not in danger : acc+=1
    return acc

def star_2():
    ingredients,allergens = parse_in("day_21_input")
    allergen_table = compile_table(ingredients,allergens)
    for ii in range(0,10):
        allergen_table = parse_table(allergen_table)
    allergen = [key for idx,key in enumerate(allergen_table)]
    allergen = sorted(allergen)
    for item in allergen:
        print(allergen_table[item])
