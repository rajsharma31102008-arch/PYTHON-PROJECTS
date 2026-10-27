#stone ,paper and scissor
# stone_paper_and_scissor__game 

import random
''' 1 for stone
    2 for paper
    3 for scissor
    '''
computer=random.choice([1,2,3])
#2dect={'stone':1,'paper':2,'scissor':3}
r=int(input("you choose (1 for stone) (2 for paper)( 3 for scissor ):"))
dects={1:'stone',2:'paper',3:'scissor'}
print(f"you enter the :{dects[r]}")
print(f"computar choice the {dects[computer]}")


if computer==r :
    print(" game draw ")
else:
    if computer==1 and r==2:
        print("you are win the game ")
    elif computer==2 and r==3:
        print(" you are the win game ")
    elif computer==3 and r==1:
        print(" you are win the game ")
    elif computer==2 and r==1:
        print(" you are loss the game ")
    elif computer==3 and r==2:
        print("you are the loss game ")
    elif computer==1 and r==3:
        print("you are  loss the game")
    else:
        print("somthing worng!!!!!!!!")



