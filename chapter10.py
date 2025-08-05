
# exercise number 6 chapter 10

from pathlib import Path
import math
from math import cos, sin
import random
from graphics import *


def firstVowel(word):
    start = 0
    if word[start].lower() == 'y':
        start = 1
    for i in range(start, len(word)):
        if word[i] in "aeiouy":       # also "aeiouy".find(word[i]) != -1
            return i

def translateWordToPL(word):
    i = firstVowel(word)
    if i == 0:
        return word+"way"
    plword = word[i:] + word[:i].lower() + "ay"
    # fix if first letter should be upper case
    if word[0].upper() == word[0]:
        plword = plword[0].upper() + plword[1:]
    return plword


def translatePhraseToPL(phrase):
    plwords = ""
    for word in phrase.split():
        plwords = plwords + translateWordToPL(word) + " "
    return plwords[:-1]


def main():
    print("Pig Latin Translator")
    with open("test_file.txt","r") as file:
        for line in file:
            print("PL translation:", translatePhraseToPL(line))




# exercise 7 chapter 10


def firstVowel(word):
    start = 0
    if word[start].lower() == 'y':
        start = 1
    for i in range(start, len(word)):
        if word[i] in "aeiouy":       # could use "aeiouy".find(word[i]) != -1
            return i


def translateWordToLF(word):
    i = firstVowel(word)
    lfword = word[:i+1]+"lf"+word[i:]
    return lfword


def translatePhraseToLF(phrase):
    lfwords = ""
    for word in phrase.split():
        lfwords = lfwords + translateWordToLF(word) + " "
    return lfwords[:-1]


def main():
    print("LF Translator")
    with open("test_file.txt","r") as file:
        for line in file:
            print("PL translation:", translatePhraseToLF(line))


# exercise 8 chapter 10


def translateFiles():
    path = Path(".")
    for file in path.glob("*.pgl"):
        with open(file,"r") as f:
            for line in f:
                print("PL translation:", translatePhraseToPL(line))
        print()    


# exercise 9 chapter 10

def censored(phrase):
    new = list(phrase)
    for i in range(len(new)):
        if len(new[i]) == 4:
            new[i] = "****"
    return str(new)

def main():
    with open("test.pgl","r") as read , open("file.pgl","w") as write:
        for line in read:
            clean = censored(line.split())
            print(clean,file=write)
   


# exrcise 10 chapter 11

def buzz_words():
    new = []
    with open("test.txt","r") as file:
        new = [word[:-1] for word in file]
    return new


def censor(phrase):
    kw = buzz_words()
    phr = list(phrase)
    for i in range(len(phrase)):
        wd = phr[i]
        if wd in kw:
            phr[i] = "*"*len(wd)
    return " ".join(phr)


def main():    
    with open("file.txt","r") as file , open("censored.txt","w") as newf:
        for phrase in file:
            cens = censor(phrase.split())
            print(cens,file=newf)


# exercise 11 chapter 10

def buzz_words():
    new = []
    with open("words.txt","r") as file:
        new = [word[:-1] for word in file]
    return new

def censor(phrase):
    kw = buzz_words()
    phr = list(phrase)
    for i in range(len(phrase)):
        wd = phr[i]
        if wd in kw:
            phr[i] = "*"*len(wd)
    return " ".join(phr)


def allFiles(oldire,newdire):
    inputP = Path(oldire)
    outputP = Path(newdire)
    for file in inputP.glob("*.txt"):
        with open(file,"r") as oldfile , open(f"{outputP}/{file.name}","w") as newfile:
            for l in oldfile:
                cens = censor(l.strip().split())
                print(cens,file=newfile)



def main():    
    with open("file.txt","r") as file , open("censored.txt","w") as newf:
        for phrase in file:
            cens = censor(phrase.split())
            print(cens,file=newf)


# exercise 12 chapter 10
# i wasn't able to finish and i read and understood the solution code
def read_file(file):
    with open(file,"r") as f:
        questions = [line[:-1] for line in f] 
    return questions



def right_answer(phrase):
    if phrase[0] == "*":
        return True 
    else:
        return False

def possibleAnswers(list):
    loc = 0
    for i in list:
        if i == '':
            pass 
        if right_answer(i):
            print(i[0:])
            right = i
        else:
            print(i)
    return right

# chapter 11 went trough the first Top-down design experience with the Proff.John

def getInput():
    ProbA = float(input("Type prob player A: "))
    ProbB = float(input("Type prob player B: "))
    n = int(input("Type how many times to repeat the game: "))
    return ProbA,ProbB,n

def simOneGame(ProbA,ProbB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while scoreA != 15 and scoreB != 15:
        if serving == "A":
            if random() < ProbA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < ProbB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA,scoreB


def simNgames(ProbA,ProbB,n):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(ProbA,ProbB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def printSummary(winsA,winsB):
    print(f"Player A won {winsA} times , Player B won {winsB} times")


def main():
    print("intro")
    ProbA, ProbB, n = getInput()
    winsA, winsB = simNgames(ProbA,ProbB,n)
    printSummary(winsA,winsB)

# exrcise 1 chapter 11

def choice(list):
    ob = randrange(len(list))
    return list[ob]


# exercise 2 chapter 11

def shuffle(list):
    for i in range(len(list)):
        loc = randrange(len(list))
        list[loc], list[i] = list[i], list[loc]    
    return list


# exercise 3 chapter 11 
# now user A serves for odds games and player B for even games
# now the user that will accomplish the half +1 total games to play stops the program and wins by default 

def getInput():
    ProbA = float(input("Type prob player A: "))
    ProbB = float(input("Type prob player B: "))
    n = int(input("Type how many times to repeat the game: "))
    return ProbA,ProbB,n

def simOneGame(ProbA,ProbB,game):
    scoreA = 0
    scoreB = 0
    if game % 2 == 0:
        serving = "B"
    else:
        serving = "A"
    while scoreA != 15 and scoreB != 15:
        if serving == "A":
            if random() < ProbA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < ProbB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA,scoreB


def simNgames(ProbA,ProbB,n):
    winsA = 0
    winsB = 0
    for i in range(1,n+1):
        scoreA, scoreB = simOneGame(ProbA,ProbB,i)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
        if winsA > (n//2)+1 or winsB > (n//2)+1:
            return winsA, winsB
    return winsA, winsB


def printSummary(winsA,winsB):
    if winsA > winsB:
        print(f"Player A was the winner")
    else:
        print("layer B was the winner")


def main():
    print("intro")
    ProbA, ProbB, n = getInput()
    winsA, winsB = simNgames(ProbA,ProbB,n)
    printSummary(winsA,winsB)

# exercise 4 chapter 11
# now the report will print : number of wins , percentage of wins , number of shuthouts , percentage of wins that are shuthouts
# SHUTHOUTS MEANS when on of the players scored 0 points in a game



def getInput():
    ProbA = float(input("Type prob player A: "))
    ProbB = float(input("Type prob player B: "))
    n = int(input("Type how many times to repeat the game: "))
    return ProbA,ProbB,n

def simOneGame(ProbA,ProbB,game):
    scoreA = 0
    scoreB = 0
    if game % 2 == 0:
        serving = "B"
    else:
        serving = "A"
    while scoreA != 15 and scoreB != 15:
        if serving == "A":
            if random() < ProbA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < ProbB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA,scoreB


def simNgames(ProbA,ProbB,n):
    winsA = 0
    winsB = 0
    shutA = 0
    shutB = 0
    for i in range(1,n+1):
        scoreA, scoreB = simOneGame(ProbA,ProbB,i)
        if scoreA > scoreB:
            winsA += 1
            if scoreB == 0:
                shutB += 1
        else:
            winsB += 1
            if scoreB == 0:
                shutA += 1
        if winsA > (n//2)+1 or winsB > (n//2)+1:
            return winsA, winsB, shutA, shutB
            
    return winsA, winsB, shutA, shutB


def printSummary(winsA,winsB,shutA,shutB):
    n = winsB+winsA
    ns = shutA+shutB
    print(f"Player A: won {winsA} games or {winsA/n:0.1%} with {shutA} shuthouts or {shutA/ns:0.1%}")
    print(f"Player B: won {winsB} games or {winsB/n:0.1%} with {shutB} shuthouts or {shutB/ns:0.1%}")



def main():
    print("intro")
    ProbA, ProbB, n = getInput()
    winsA, winsB, shutA, shutB = simNgames(ProbA,ProbB,n)
    printSummary(winsA,winsB,shutA,shutB)


# exercise 5 chapter 11
# in this program i'm going to create a simulation of volleyball game
# the game works the same as raquetball with the difference that the team needs 2 points more than the other to win

def main():
    printIntro()
    probA, probB, n = getInputs()
    RwinsA, RwinsB = RallysimNGames(n, probA, probB)
    SidewinsA, SidewinsB = SideOutsimNGames(n, probA, probB)
    printSummary(RwinsA, RwinsB, SidewinsA, SidewinsB)


def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B".  The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.\n")


def getInputs():
    # Returns the three simulation parameters
    print("This is for the game played with rally ")
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


def SideOutsimNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = SideOutsimOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def RallysimNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = RallysimOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def SideOutsimOneGame(probA, probB):
    # Simulates a single game or racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not SideOutgameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA +=  1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB +=  1
            else:
                serving = "A"
    return scoreA, scoreB


def SideOutgameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    if (a > b+2 and a >= 25) or (b > a+2 and b >= 25):
        return True

def RallysimOneGame(probA, probB):
    # Simulates a single game or racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not RallygameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA +=  1
            elif random() < probB:
                scoreB += 1
                serving = "B"
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB +=  1
            elif random() < probA:
                scoreA += 1
                serving = "A"
            else:
                serving = "A"
    return scoreA, scoreB


def RallygameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    if (a > b+2 and a >= 25) or (b > a+2 and b >= 25):
        return True


def printSummary(RwinsA, RwinsB, SwinsA, SwinsB):
    # Prints a summary of wins for each player.
    n = RwinsA + RwinsB
    print("\nGames simulated:", n)
    print()
    print("Game simulated with Rally scoring")
    print(f"Wins for A: {RwinsA} ({RwinsA/n:0.1%})")
    print(f"Wins for B: {RwinsB} ({RwinsB/n:0.1%})")
    print()
    print("Game simulated with Side out scoring")
    print(f"Wins for A: {SwinsA} ({SwinsA/n:0.1%})")
    print(f"Wins for B: {SwinsB} ({SwinsB/n:0.1%})")



# exercise 9 chapter 11 
# simulate the game of CRAPS


def roll():
    return (randrange(1,6) + randrange(1,6))

def check(roll):
    if roll in [2,3,12]:
        return False
    elif roll in [7,11]:
        return True
    else:
        return "keep rolling"

def mainRolling():
    initRoll = roll()
    verify = check(initRoll)
    if verify == "keep rolling":
        while True:
            r = roll()
            if r == 7:
                return 0
            if r == initRoll:
                return 1
    elif verify:
        return 1
    else:
        return 0


def intro():
    print("Hi this a game called Craps , you roll one time")
    print("If your roll is equal to 2,3,12 you lose , if the rool")
    print("is equal to 7 or 11 you will win. ")
    print("If any of these it will keep rolling untill 7 == lose or if the same value of the initial roll == win")
    print()
    n = int(input("Type here how many games you want to play"))
    return n


def main():
    n = intro()
    win = 0
    for i in range(n):
        game = mainRolling()
        win += game
    print(f"You won {win} games with a probability of {win/n:0.1%}")



# exercise 10 chapter 11


def printIntro():
    print("This program is going to play a Blackjack from the dealer point of view")
    print("if the dealer reaches reaches > 21 will bust instead if picks an ace and adding 10 would give a value between 17 and 21 the value of ace changes from 1 to 11 for that draw")
    print("The dealer will do 1000 draws in total")


def checkFace(draw):
    if draw > 10:
        draw = 10
        return draw
    else:
        return draw
    
def checkAce(total):
    if 17 <= total+10 <= 21:
            tt = total + 10 
            return tt
    else:
        return total
    
def playThegame(value):
    total = 0
    has_ace = False
    draw = checkFace(value)
    while total < 17:
        total += draw
        if draw == 1 or has_ace:
            has_ace = True
            total = checkAce(total)
        draw = checkFace(randrange(1,14))
    return total




def main():
    printIntro()
    for card in range(1,11):
        bust = 0
        for i in range(1000):
            points = playThegame(card)
            if points > 21:
                bust += 1
        print(f"With the card of value {card} , The dealer busted {bust} times with a probability of {bust/1000:0.1%}")


# exercise 12 chapter 11

def coord():
    return 2 * random() - 1



def checkLies(x,y):
    hypot = math.sqrt(x*x + y*y)
    if hypot <= 1:
        return True
    else:
        return False


def operation(darts):
    h = 0
    for i in range(darts):
        x,y = coord(), coord()
        where = checkLies(x,y)
        if where:
            h += 1
    return 4 * h/darts





def mainEstimatePi():
    darts = 1000 #printIntro()
    pi = operation(darts)
    print(f"This is the value of pi {pi}")


# exercise 13 chapter 11



def throwDice():
    oneKind = False
    throwns = []
    for i in range(5):
        new = randrange(1,7)
        throwns.append(new)
    if throwns.count(new) == 5:
        return True


def probab_dice():
    rolls = 1000
    kind = 0
    for i in range(rolls):
        dice = throwDice()
        if dice:
            kind += 1
    print(f"{kind/rolls}") 

# exercise 14 chapter 11


def coinFlip(n):
    step = 0
    for i in range(n):
        if random() < 0.5:
            flip = coinFlip()
            if flip:
                steps += 1
            else:
                steps -= 1
    return abs(steps)

def randomWalk():
    askLenght = int(input("Type here the sidelength of the sidewalk: "))
    askWalks = int(input("Type here how many walks: "))
    distance = 0
    for walks in range(askWalks):
        steps = coinFlip(n)
        distance += abs(steps)
    print(f"You ended up being {distance/askWalks} steps from your starting point")



# exercise 15 cahpter 11
# i read the code for the count of the stepped on squares , i did figured out but no wi unrstood it and solved the last things by myself

def squares(length):
    squares = [0] * length
    return squares



def coinFlip(length):
    pos = 0
    steps = 0
    counts = squares((length*2+1))
    while abs(pos) <= length:
        counts[length-pos] = counts[length-pos] + 1
        if random() < 0.5:
            pos -= 1
        else:
            pos += 1
        steps += 1

    return counts,steps

def Newlist(oldone,newone):
    if oldone != 0:
        for i in range(len(oldone)):
            oldone[i] += newone[i]
        return oldone 
    else:
        return newone


def randomWalk():
    askLength = int(input("Type here the sidelength of the sidewalk: "))
    askWalks = int(input("Type here how many walks: "))
    update = 0
    for walks in range(askWalks):
        counts,steps = coinFlip(askLength) 
        update = Newlist(update,counts)
    return update, steps
    print(f"You ended up being {sum(distances)/askWalks} steps from your starting point on avg and Counts : \n {distances}")


# exercise 16 chapter 11




def coinFlip(length):
    lateral, ForwBackw = 0
    for i in range(length):
        step = random()
        if step < .25:
            lateral += 1
        elif step < .5:
            lateral -= 1
        elif step < .75:
            ForwBackw += 1
        else:
            ForwBackw -= 1

    return (ForwBackw**2 + lateral**2)**.5


def randomWalk():
    askLength = int(input("Type here the sidelength of the sidewalk: "))
    askWalks = int(input("Type here how many walks: "))
    steps = 0
    for walks in range(askWalks):
        n = coinFlip(askLength) 
        steps += n
    return steps / askWalks




# exercise 17 chapter 17


def Windowgen():
    win = GraphWin("Window",500,500)
    win.setCoords(0,0,200,200)
    win.setBackground("black")
    return win


def randomStep(x,y):
    angle = random() * 2 * math.pi
    x += cos(angle)
    y += sin(angle)
    return x,y

def DrawStep(win,x,y,oldx,oldy):
    step = Line(Point(oldx,oldy),Point(x,y))
    step.setFill("white")
    step.draw(win)
    return step


def main():
    askLength = int(input("Type here the sidelength of the sidewalk: "))
    oldx = 100
    oldy = 100
    win = Windowgen()
    for i in range(askLength):
        x, y = randomStep(oldx,oldy)
        DrawStep(win,x,y,oldx,oldy)
        oldx, oldy = x, y
    win.getMouse()


# exercise 2 chapter 12
# creating a very simple not-so-good-but-works coinflip window program

from button import Button

class Coin:

    def __init__(self,win,center,size):
        self.win = win
        self.center = center
        self.radius = 0.3 * size
        self.x,self.y = center.getX() , center.getY()
        
    def heads(self):
        x,y = self.x,self.y
        r = self.radius
        sr = r/4  # i need this in order to place the mouth and eye
        coin = Circle(Point(x,y),r)
        face = Circle(Point(x,y),r/2)
        smile = Oval(Point(x-sr,y-sr),Point(x+sr,y-(0.6*sr)))
        eye,reye = Circle(Point(x-sr,y),sr/2),Circle(Point(x+sr,y),sr/2)

        # draw all the object
        coin.setFill("yellow")
        coin.draw(self.win)
        face.setOutline("black")
        face.setFill("white")
        face.draw(self.win)
        smile.setFill("gray")
        smile.draw(self.win)
        eye.setFill("black")
        eye.draw(self.win)
        reye.setFill("black")
        reye.draw(self.win)


    def tail(self):
        win = self.win
        x,y = self.x,self.y
        r = self.radius
        coin = Circle(Point(x,y),r)
        text = Text(Point(x,y),"TAIL")


        #draw the object
        coin.setFill("yellow")
        coin.draw(win)
        text.setSize(12)
        text.setFill("black")
        text.draw(win)
    

def Windowgen():
    win = GraphWin("Window",500,500)
    win.setCoords(-10,-10,10,10)
    win.setBackground("black")
    return win

def Createtext(win,testo,x,y):
    testo = Text(Point(x,y),testo)
    testo.setSize(13)
    testo.setFill("white")
    testo.draw(win)
    return testo

def Coinflip():
    if random() < 0.5:
        return True
    else:
        return False


def main():
    win = Windowgen()
    text = Createtext(win,"Type in the window to <esc> ",0,0)
    text.undraw()
    coin = Coin(win,Point(0,0),10)
    coin.heads()
    b = Button(win,Point(0,-5),4,2,"BUTTON")
    b.activate()
    text = Createtext(win,"Type in the window to <esc> ",0,5)
    tap = win.getMouse()
    text.undraw()
    while b.clicked(tap):
        if Coinflip():
            coin.heads()
        else:
            coin.tail()
        tap = win.getMouse()



# exercise 2 chapter 12 second mini-project

def Windowgen():
    win = GraphWin("Window",500,500)
    win.setCoords(-10,-10,10,10)
    win.setBackground("black")
    return win

def Createtext(win,testo,x,y):
    testo = Text(Point(x,y),testo)
    testo.setSize(13)
    testo.setFill("white")
    testo.draw(win)
    return testo

def ChangeColorshape():
    win = Windowgen()
    Createtext(win,"Type one of the three buttons to change color to the shape \n To esc type in the window ",0,0)
    win.getMouse()

    # create a shape that change color
    shape = Circle(Point(0,-5),2)
    shape.setFill("white")
    shape.setOutline("black")
    shape.draw(win)

    #create buttons for green,yellow,red
    green = Button(win,Point(-5,5),4,2,"green","GREEN")
    green.activate()
    red = Button(win,Point(0,5),4,2,"red","RED")
    red.activate()
    yellow = Button(win,Point(5,5),4,2,"yellow","YELLOW")
    yellow.activate()
    tap = win.getMouse()

    

    while True:
        if yellow.clicked(tap):
            shape.setFill("yellow")
        elif green.clicked(tap):
            shape.setFill("green")
        elif red.clicked(tap):
            shape.setFill("red")
        else:
            break
        tap = win.getMouse()


# exercise 2 chapter 12


        

def Windowgen():
    win = GraphWin("Window",500,500)
    win.setCoords(-10,-10,10,10)
    win.setBackground("black")
    return win

def Createtext(win,testo,x,y):
    testo = Text(Point(x,y),testo)
    testo.setSize(13)
    testo.setFill("white")
    testo.draw(win)
    return testo

def DrawButtons():
    b = random.randrange(0,4)
    if b == 1:
        return 0
    elif b == 2:
        return 1
    else:
        return 2
    

def checkclicked(first,second,third,tap):
    if first.clicked(tap):
        return 0
    elif second.clicked(tap):
        return 1
    elif third.clicked(tap):
        return 2
    else:
        return None

def ThreeButtonMonte():
    win = Windowgen()


    # Create buttons
    firstD = Button(win,Point(-5,5),4,2,"gray","DOOR 1")
    firstD.activate()
    secondD = Button(win,Point(0,5),4,2,"gray","DOOR 2")
    secondD.activate()
    thirdD = Button(win,Point(5,5),4,2,"gray","DOOR 3")
    thirdD.activate()
    quit = Button(win,Point(0,-7),4,2,"red","QUIT")
    quit.activate()
    buttons = [firstD,secondD,thirdD]

    # Print text setting the game
    intro = Createtext(win,"Type one of the three buttons and see if you win!",0,0)
    winner, looser = 0, 0
    countw = Createtext(win,f"Win:{winner}",-5,-5)
    countl = Createtext(win,f"Lost:{looser}",5,-5)
    tap = win.getMouse()
    intro.undraw()



    # Loop game
    while not quit.clicked(tap):
        select = DrawButtons()
        typed = checkclicked(firstD,secondD,thirdD,tap)

        if typed == None:
            pass
        elif  buttons[select] == buttons[typed]:
            won = Createtext(win,"You are the Winner! Type in the window to play again",0,0)
            winner += 1
            countw.undraw()
            countw = Createtext(win,f"Win:{winner}",-5,-5)
            win.getMouse()
            won.undraw()
            
        else:
            lost = Createtext(win,f"You Lost The answer was Door {select+1}!\n Type in the window to play again",0,0)
            looser += 1
            countl.undraw()
            countl = Createtext(win,f"Lost:{looser}",5,-5)
            win.getMouse()
            lost.undraw()

        # ask to play again
        type = Createtext(win,"Type one of the three buttons and see if you win!",0,0)
        tap = win.getMouse()
        type.undraw()



ThreeButtonMonte()





    






