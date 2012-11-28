#! /usr/bin/env python

from chickenClasses import *

def main():
    
    endGame = False
    
    chicken = item('chicken', True, True, True)
    onion = item('onion', True, True, True)
    pepper = item('pepper', True, True, True)
    cheese = item('cheese', True, True, True)
    salt = item('salt', True, False, False)
    blackPepper = item('blackpepper', True, False, False)
    bread = item('bread', True, True, False)
    stove = item('stove', False, False, False)
    oven = item('oven', False, False, False)
    
    things = container([chicken, onion, pepper, cheese, salt, blackPepper, bread, stove, oven])
    
    room = container([chicken, onion, pepper, cheese, salt, blackPepper, bread, stove, oven])
    player = container([])
    
    look1 = look(['look', 'peek', 'gaze'], {'room': room, 'inventory': player})
    cook1 = cook(['cook', 'make'], [])
    put1 = put(['put', 'place'], [])
    score1 = scoring(['score', 'points'], [])
    eat1 = eat(['eat', 'munch', 'snack', 'devour', 'slam'], [])
    
    points = score()
    
    print """You are in a kitchen."""
    
    verbs = verbiage([look1, cook1, put1, score1, eat1])
    
    
    while True:
        thingIsReal = False
        thingsToUse = []
        s = raw_input('>')
        t = s.split()
        
        
        for x in t:
            if x == 'exit':
                return
        
        
        if t[0] in verbs.listSyns():
            for x in verbs.verbs:
                if t[0] in x.synonyms:
                    if t[1:] == []:
                        x.do([], points)
                    else:
                        for noun in t[1:]:
                            if noun in things.names():
                                thingIsReal = True
                                thingsToUse.append(things.containerDict()[noun])
                            else:
                                print 'I do not understand "' + noun + '"'
                        
                        if thingIsReal:
                            #print thingsToUse
                            x.do(thingsToUse, points)
        
        else:
            print 'You cannot "' + t[0] + '"'



if __name__ == "__main__":
    main()
