import re

in_f = open("day_04_input","r")
p_list = in_f.readlines()
in_f.close()

def check_1(fields,item): # fields is a list of patterns
    if len(item) < len(fields) : return False
    else:
        matches = 0
        for entry in item:
            entry = re.sub("\s","",entry)
            for ff in fields:
                if ff==fields[2]:
                    if entry[0:4] == "eyr:":
                        print(ff)
                        print(entry)
                        print(ff.match(entry)!=None)
                        print("\n")
                if ff.match(entry)!=None: matches += 1
        if len(fields) == matches: return True
        else: return False

   
def read_pass(passport):
    reading = []
    for item in passport : reading+=re.split(" ",item)
    return reading

fields_1 = [re.compile(r'byr:+'),re.compile(r'iyr:+'),re.compile(r'eyr:+'),re.compile(r'hgt:+'),re.compile(r'hcl:+'),re.compile(r'ecl:+'),re.compile(r'pid:+')]

fields_2 = []
fields_2 += [re.compile(r'byr:19[2-9][0-9]|byr:200[0-2]')]
fields_2 += [re.compile(r'iyr:201[0-9]|iyr:2020')]
fields_2 += [re.compile(r'eyr:(202[0-9]|2030)')]
fields_2 += [re.compile(r'hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)')]
fields_2 += [re.compile(r'hcl:#([0-9a-f]{6})')]
fields_2 += [re.compile(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)')]
fields_2 += [re.compile(r'pid:[0-9]{9}$')]


def star_1(p_list,fields):
    valid = 0
    passport = []
    for item in p_list:
        if item == "\n" :
            if check_1(fields,read_pass(passport)) : valid +=1
            passport =[]
        else : 
            passport += [item]
    if passport!=[] :
        if check_1(fields,read_pass(passport)) : valid +=1
    return valid

print(star_1(p_list,fields_1))
print(star_1(p_list,fields_2))


