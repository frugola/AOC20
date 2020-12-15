import time

nbrs = [19,0,5,1,10,13]
test = [0,3,6]

def game(nbrs,stop):
    ii = len(nbrs)
    while ii<stop:
        if ii%10000==0:print(ii)
        spoken = nbrs[-1]
        where = [idx for idx,n in enumerate(nbrs[0:-1]) if n==spoken]
        if where==[]: nbrs+=[0]
        else: nbrs+=[ii-where[-1]-1]
        ii+=1
    return nbrs

def game_fast(nbrs,stop):
    ii = len(nbrs)-1
    spoken = nbrs[-1]
    dict_n = {n:idx for idx,n in enumerate(nbrs)}
    while ii<stop:
        if spoken in dict_n and dict_n[spoken]<ii : new_spoken=ii-dict_n[spoken]
        else : new_spoken = 0
        dict_n[spoken] = ii
        spoken=new_spoken
        ii+=1
    return dict_n

def star_1(nbrs,target):
    nbrs = game(nbrs,target)
    print(nbrs[-1])

def star_2(nbrs,target):
    dict_n = game_fast(nbrs,target)
    key_list = list(dict_n.keys())
    val_list = list(dict_n.values())
    print(key_list[val_list.index(target-1)])

star_1(nbrs,2020)
start = time.time()
star_2(nbrs,30000000)
print(time.time()-start)
