import re

in_f = open("day_16_input","r")
dump = in_f.readlines()
in_f.close()

in_f = open("test","r")
test = in_f.readlines()
in_f.close()

in_f = open("test_2","r")
test_2 = in_f.readlines()
in_f.close()


def parse(dump):
    nearby = []
    fields = {}
    for item in dump :
        item = re.sub("\n","",item)
        item = re.split(": ",item)
        if len(item)==2 and item[1]!="":
            # part 1 is name
            # part 2 is intervals
            itv = re.split(" or ",item[1])
            itv = [re.findall("\d+",ii) for ii in itv]
            A = {ii for ii in range(int(itv[0][0]),int(itv[1][1])+1)}
            B = {ii for ii in range(int(itv[0][1])+1,int(itv[1][0]))}
            A-=B
            fields[item[0]] = A
        elif len(item)==1 and item[0]!="" :
            nearby += [re.findall("\d+",item[0])]
            if nearby[-1]!=[]: nearby[-1] = [int(ii) for ii in nearby[-1]]
            else : nearby = nearby[:-1]
    my_ticket = nearby[0]
    nearby = nearby[1:]
    return fields, my_ticket, nearby

def error_ticket(ticket,sets):
    validate = [1 for field in ticket]
    for idx,field in enumerate(ticket):
        for s in sets:
            if field in s : validate[idx]=0
    if sum(validate)==0 : return 0
    else : 
        error = sum([validate[idx]*ticket[idx] for idx in range(0,len(ticket))])
        return error
        
def star_1(dump):
    err = 0
    fields,my_ticket,nearby = parse(dump)
    sets = []
    for idx,key in enumerate(fields):
        sets += [fields[key]]
    for ticket in nearby:
        err += error_ticket(ticket,sets)
    print(err)

def field_valid(s,col):
    check = [1 for c in col if c in s]
    if sum(check) == len(col): return True
    else: return False

def star_2(dump):
    fields,my_ticket,nearby = parse(dump)
    valid = []
    field_map = {}
    sets = []
    keys = []
    for idx,key in enumerate(fields):
        sets += [fields[key]]
        keys += [key]
    for ticket in nearby:
        if error_ticket(ticket,sets) == 0 : valid += [ticket]
    # assign the fields
    # make a list of the columns (idx of the column is idx of the field)
    columns = []
    for idx in range(0,len(valid[0])):
        columns += [[ticket[idx] for ticket in valid]]
    # for every column, check how many fields are ok
    # if only one field is ok, assign field to index
    while fields != {}:
        to_del = None
        # for every column
        for id_col,col in enumerate(columns):
            ff_checks = 0
            # for every field
            for id_ff,ff in enumerate(fields):
                # check if field valid
                if field_valid(fields[ff],col):
                    ff_checks += 1
                    last_ff = ff
            if ff_checks == 1: # only one field ok for the col
                field_map[last_ff]=id_col
                del fields[last_ff]
                to_del = id_col
    print(fields.keys())
    print(field_map)
    # find the product
    prod = 1
    for idx,key in enumerate(field_map):
        if re.findall("departure",key)!=[]:
            prod=prod*my_ticket[field_map[key]]
    print(prod)
                

star_1(dump)
star_2(dump)
