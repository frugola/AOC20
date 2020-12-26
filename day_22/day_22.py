from copy import deepcopy

def parse_in(filename):
    in_f = open(filename,"r")
    dump = in_f.readlines()
    one = []
    two = []
    play_one = False
    play_two = False
    for item in dump: 
        item = item.strip("\n")
        if item == "Player 1:": 
            play_one = True
            play_two = False
        elif item == "Player 2:":
            play_one = False
            play_two = True
        elif item == "": pass
        elif play_one and not play_two:
            one += [int(item)]
        elif not play_one and play_two:
            two += [int(item)]
    return one,two

def round(one,two):
    draw_one = one[0]
    draw_two = two[0]
    if draw_one > draw_two:
        one = one[1:]+[draw_one,draw_two]
        two = two[1:]
    elif draw_two > draw_one:
        two = two[1:]+[draw_two,draw_one]
        one = one[1:]
    return one,two

def game(one,two):
    while one!=[] and two!=[]:
        one,two = round(one,two)
    return one,two

def round_complete(one,two,prev_games):
    #print(one)
    #print(two)
    one_wins = False
    two_wins = False
    # prev games is a list
    # each element is a (str(one),str(two))
    if (" ".join([str(i) for i in one]), " ".join([str(i) for i in two])) in prev_games:
        print("DEJA VU")
        one_wins = True
        two = []
    else:
        prev_games += [(" ".join([str(i) for i in one])," ".join([str(i) for i in two]))]
        draw_one = one[0]
        draw_two = two[0]
        if len(one)-1 >= draw_one and len(two)-1 >= draw_two:
            new_one = deepcopy(one)[1:draw_one+1]
            new_two = deepcopy(two)[1:draw_two+1]
            new_one_wins,new_one,new_two_wins,new_two = game_complete(new_one,new_two)
            # new_one_wins,new_two_wins =  GAME recursion new_one,new_two
            if new_one_wins:
                one = one[1:]+[draw_one,draw_two]
                two = two[1:]
            elif new_two_wins:
                two = two[1:]+[draw_two,draw_one]
                one = one[1:]
        elif draw_one > draw_two :
            one = one[1:]+[draw_one,draw_two]
            two = two[1:]
            one_wins = True
        elif draw_two > draw_one :
            two = two[1:]+[draw_two,draw_one]
            one = one[1:]
            two_wins = True
    return one_wins,one,two_wins,two,prev_games

GAMES = 0

def game_complete(one,two):
    global GAMES
    GAMES += 1
    print("new game", GAMES)
    print(one)
    print(two)
    prev_games = []
    while one!=[] and two!=[]:
        one_wins,one,two_wins,two,prev_games = round_complete(one,two,prev_games)
    print("END GAME")
    return one_wins,one,two_wins,two

def score(deck):
    acc = 0
    for idx,ii in enumerate(range(len(deck)-1,-1,-1)):
        acc += (idx+1)*deck[ii]
    return acc

def star_1(filename):
    one,two = parse_in(filename)
    one,two = game(one,two)
    if one != []:
        print(score(one))
    elif two != []:
        print(score(two))

def star_2(filename):
    one,two = parse_in(filename)
    one_wins,one,two_wins,two = game_complete(one,two)
    if one != []:
        print(score(one))
    elif two != []:
        print(score(two))

star_1("day_22_input")
#star_2("test")
star_2("day_22_input")

