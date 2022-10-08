import random
user=input("enter the either sissor(s),paper(p),rock(r) \n")
print("you choose : ",user)
print("now its computer chance to choose")
randomNo=random.randint(1,3)
if randomNo == 1:
    computer="s"
elif randomNo == 2:
    computer="p"
elif randomNo == 3:
    computer="r"        
print("computer choose : ",computer)
def gameWin(computer, user):
    if (computer==user):
        print("game is tie")
    elif((computer=="s" and user =="p")or(computer=="r" and user =="s")or(computer=="p" and user =="r")) :
        print("you loose the game") 
    elif((computer=="p" and user =="s")or(computer=="r" and user =="p")or(computer=="s" and user =="r")) :
        print("you are the bloody winner") 
    else:
        print("entered value is not in game's domain")
gameWin(computer,user)