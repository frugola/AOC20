import re

colors = []  # list of lists; each internal list gets the colors of one line
quantities = [] # list of lists; each internal list gets the quantities in one line

in_f = open("day_07_input","r")
for line in in_f:
    line = re.sub("no other","0 other",line)
    tmp_colors = []
    tmp_quantities = []
    external,internal = re.split("contain",line)
    tmp_quantities += [1]
    tmp_colors += [external[:-6]]
    internal = re.sub("\n","",internal)
    internal = re.sub("\.","",internal)
    bag_list = re.split(",",internal)
    for bag in bag_list:
        tmp_quantities += [int(o) for o in re.findall("\d+",bag)]
        tmp_colors += [re.sub("( bags| bag)","",(re.sub("\d+","",bag)))[2:]]
    colors += [tmp_colors]
    quantities += [tmp_quantities]
in_f.close()


def direct_in(target_col,colors): # returns the list of the bags containing the target color
    containers = []
    for line in colors:
        for idx,item in enumerate(line):
            if idx > 0 and item == target_col:
                if line[0] not in containers: containers +=[line[0]]
    return containers


def star_1(wanted_bag):
    containers = direct_in(wanted_bag,colors)
    # add item in containers if not already in
    # check only the new added items
    to_check = [item for item in containers]

    while len(to_check)>0:
        to_check_next = []
        for tar_c in to_check:
            new_items = direct_in(tar_c,colors)
            for item in new_items:
                if item not in containers: 
                    containers += [item]
                    to_check_next += [item]
        to_check = [o for o in to_check_next]

    return(containers)


def contents(bag_c): # get the bags inside a bag
    for idx,line in enumerate(colors):
        if line[0]==bag_c:
            return {line[ii]:quantities[idx][ii] for ii in range(1,len(line))}

def star_2(target):
    total = 0
    to_open = contents(target)
    while to_open != {}:
        total += sum(to_open[ii] for ii in to_open)
        next_to_open = {}
        for col_key in to_open:
            if contents(col_key) != None:
                tmp = contents(col_key)
                for item in tmp:
                    tmp[item] = tmp[item]*to_open[col_key]
                for item in tmp:
                    if item in next_to_open:
                        next_to_open[item] = next_to_open[item]+tmp[item]
                    else:
                        next_to_open[item] = tmp[item]
            else: pass
        to_open = {ii:next_to_open[ii] for ii in next_to_open}
    return total


print(len(star_1("shiny gold")))
print(star_2("shiny gold"))






        
