class item:
    
    def __init__(self, nameStr, canHold, canCook, canGoOnBread):
        self.name = nameStr
        self.holdable = canHold
        self.cookable = canCook
        self.breadable = canGoOnBread
        self.onBread = False
        self.cooked = False
    
    def canTake(self):
        return self.holdable
    
    def canCook(self):
        return self.cookable
    
    def __str__(self):
        return self.name
    
class score:
    
    def __init__(self):
        self.points = 0
    
    def addPoint(self):
        self.points += 1

class container:
    """Containers hold things. This is the base class for actors and rooms."""
    def __init__(self, things):
        self.contents = things

    def listContents(self):
        return self.contents

    def add(self, thing):
        self.contents.append(thing)

    def remove(self, thing):
        self.contents.remove(thing)

    def take(self, thing, loser):
        self.add(thing)
        loser.remove(thing)
    
    def names(self):
        result = []
        for x in self.contents:
            result.append(x.name)
        return result
    
    def containerDict(self):
        result = {}
        for x in self.contents:
            result[x.name] = x
        return result

    def __str__(self):
        result = ''
        for x in self.contents:
            result += x.name
            result += '\n'
        return result[:-1]


class verbiage:
    def __init__(self, words):
        self.verbs = words
        
    def listSyns(self):
        result = []
        for x in self.verbs:
            for synonyms in x.listSynonyms():
                result.append(synonyms)
        return result

            
class verb:
    """Verbs have synonyms and valid objects."""
    def __init__(self, words, valids):
        self.synonyms = words
        self.valids = valids
        
    def listSynonyms(self):
        return self.synonyms
    
    def canDo(self, words):
        if self.valids.contains(word):
            return True
        return False
    
class look(verb):

    def do(self, things, score):
       # print thing        
        if things == []:
            print "You see"
            for y in self.valids['room'].contents:
                print y
        else:        
           for x in things:
                if x in self.valids:
                    print "You see"
                    #print x
                    #print self.valids[x]
                    for y in self.valids[x].contents:
                        print y

class cook(verb):
    
    def do(self, things, score):
        for thing in things:
            if thing.cookable and not thing.cooked:
                thing.cooked = True
                print "You cooked the " + thing.name
                score.addPoint()
            elif thing.cooked:
                print "You already cooked the " + thing.name + "!"
            else:
                print "You cannot cook the " + thing.name + "!"


class put(verb):
    def do(self, things, score):
        
        bready = False
        breadPlace = 0
        
        if len(things) == 0 or len(things) == 1:
            print "Be more specific!"
            return
        
        for x in things:
            if x.name == "bread":
                bready = True
                bread = x
        
        if not bready:
            print "Cannot put on that"
            return
        
        things.remove(bread)
        for x in things:
            if x.breadable and x.cooked and not x.onBread:
                print "You put the " + x.name + ' on the bread!'
                score.addPoint()
                x.onBread = True
            elif not x.breadable:
                print "The " + x.name + " cannot go on the bread!"
            elif not x.cooked:
                print "The " + x.name + " is not cooked yet!"
            else:
                print "The " + x.name + " is already on the bread!"

class scoring(verb):
    
    def do(self, things, score):
        print "Your score is " + str(score.points) + " out of 10 points"
        
        
class eat(verb):
    
    def do(self, things, score):
        score.addPoint()
        print "You ate your chickencheese! Congratulations!"
        print "Your score is " + str(score.points) + " out of 10!"
        exit(0)