import re

money = []

in_f = open("day_01_input","r")
for line in in_f:
    money += [int(re.sub("\s","",line))]
in_f.close()

def star_01(money):
    for ii in range(0,len(money)):
        for kk in range(ii+1,len(money)):
            if money[ii]+money[kk] == 2020:
                return money[ii]*money[kk]
                break

def star_02(money):
    for ii in range(0,len(money)):
        for kk in range(ii+1,len(money)):
            for jj in range(kk+1,len(money)):
                if money[ii]+money[kk]+money[jj] == 2020:
                    return money[ii]*money[kk]*money[jj]
                    break
 


print(star_01(money))
print(star_02(money))

