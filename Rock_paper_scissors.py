#Rock_Paper_scissors game
import random
from random import choice

user=0
comp=0

def comp_act():
    actCom=['R','P','S']
    return choice(actCom)

def gameplay():
    global comp
    global user
    if actUser==comp_act():
        result='Its a Tie'
        return result
    elif actUser=='P' and comp_act()=='R' or actUser=='S' and comp_act()=='P' or actUser=='R'and comp_act()=='S':
        comp+=1
        result='Computer wins!!!'
    elif actUser not in ['P',"S",'R','Exit']:
        result='Invalid entry!!'
    else:
        result='User Wins!!!'
        user+=1
    print(result)   
    print('''User Score--->{}
    computer Score--->{}'''.format(user,comp))
    

while 1:
    print()
    print('''        'S'-->Scissors
        'R'-->Rock
        'P'-->Paper
        'Exit'-->To end the game.''')
    print()
    actUser=input('Enter: ')
    if actUser=='Exit':
        print('Ending game!!!')
        break
    gameplay()
    
           

    
