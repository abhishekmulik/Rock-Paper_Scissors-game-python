import random
from random import choice
user_score=0
comp_score=0
class Action:
    def __init__(self):
        self.rock='R'
        self.paper='P'
        self.scissors='S'
        

class Comp_play(Action):
    def __init__(self):
        super().__init__()
    def comp_act(self):
        self.actCom=[self.rock,self.scissors,self.paper]
        return choice(self.actCom)


class gamePlay(Comp_play): 
    
    def play(self):
        global user_score
        global comp_score
        
        if actUser==super().comp_act():
            self.result='Its a Tie!!! try again!!'
        elif (actUser=='R' and super().comp_act()=='P') or (actUser=='P' and super().comp_act()=='S') or (actUser=='S'and super().comp_act())=='R':
            self.result='Computer wins!!!'
            comp_score+=1
        elif actUser not in ['P',"S",'R']:
            self.result='Invalid entry!!'
        elif actUser=='Exit':
            self.result='Ending game!!!'
        else:
            self.result='User Wins!!!'
            user_score += 1
        print()
        print(self.result)
        print()
        print('''User Score--->{}
        computer Score--->{}'''.format(user_score,comp_score))
        
    
while 1: 
    gm=gamePlay()
    print('*------------*')
    actUser=input('Enter your choice: ')
    if actUser=='Exit':
        print('Ending game!!!! Thankyou')
        break
    gm.play()
    
    





