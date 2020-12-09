import re


def is_sum(w,p,n): # window (25 in game), pointer (element to check), numbers
    flag = False
    for ii in range(p-w,p):
        for kk in range(ii,p):
            if (n[ii]!=n[kk]) and ((n[ii]+n[kk])==n[p]):
                flag = True
                break
    return flag


def star_1(w,n):
    for p in range(w,len(n)):
        if is_sum(w,p,n)==False: return(n[p])


def star_2(w,nbs):
    target = star_1(w,nbs)
    res = None
    for i in range(0,len(nbs)-1):
        k = i
        while k<len(nbs) and sum(nbs[i:k+1]) < target:
            k+=1
           # if i == 0 and k < 5 : print((nbs[i:k+1]),nbs[i],nbs[k],sum(nbs[i:k+1]))
            if sum(nbs[i:k+1])==target: 
                tmp = nbs[i:k+1]
                print(min(tmp)+max(tmp))
                break

nbs = []

in_f = open("day_09_input")
for line in in_f:
    nbs += [int(re.findall("\d+",line)[0])]
in_f.close()

   
print(star_1(25,nbs))
star_2(25,nbs)
