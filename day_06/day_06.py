import re
from string import ascii_lowercase

def answers(entries):
    ans = 0
    for item in entries:
        for letter in ascii_lowercase:
            if letter in item: ans+=1
    return ans

def answers_2(item):
    ans = 0
    for letter in ascii_lowercase:
        times = [1 for word in item if letter in word]
        if sum(times) == len(item) : ans+=1
    return ans


def star_1():
    in_f = open("day_06_input","r")
    entries = in_f.readlines()
    in_f.close()
    entries = re.split("\n\n","".join(entries))
    entries = [re.sub("\n","",item) for item in entries]
    return answers(entries)

def star_2():
    in_f = open("day_06_input","r")
    entries = in_f.readlines()
    in_f.close()
    entries = re.split("\n\n","".join(entries))
    print(entries)
    entries = [re.split("\n",item) for item in entries]
    ans = 0
    for item in entries:
        if item[-1]=="" : item=item[0:-1]
        ans += answers_2(item)
    return ans


print(star_1())
print(star_2())


