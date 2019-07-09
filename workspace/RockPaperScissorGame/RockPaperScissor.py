import random

choices=['Rock','Paper','Scissor']

def computeSystemInput():
    return random.choice(choices)

def computeWinner(usrChoice,sysChoice):
    if(usrChoice==sysChoice):
        print("It's a tie!!")
    if(usrChoice=='Rock'):
        if(sysChoice=='Paper'):
            print("You lose!! Paper covers Rock.")
        elif(sysChoice=='Scissor'):
            print("Congratulations!! You won! Rock crushes Scissor")
    elif(usrChoice=='Paper'):
        if(sysChoice=='Scissor'):
            print("You lose!! Scissor cuts Paper.")
        elif(sysChoice=='Rock'):
            print("Congratulations!! You won! Paper covers Rock.")
    elif(usrChoice=='Scissor'):
        if(sysChoice=='Rock'):
            print("You lose!! Rock crushes Scissor.")
        elif(sysChoice=='Paper'):
            print("Congratulations!! You won! Scissor cuts Paper.")
            
def play():    
    userchoice=input("Please enter your choice among [Rock,Paper,Scissor]")
    print("Your choice is : ",userchoice)
    if userchoice in choices:
        systemchoice=computeSystemInput()
        print("System's choice is : ",systemchoice)
        computeWinner(userchoice,systemchoice)
    else:
        while userchoice not in choices:
            userchoice=input("Invalid choice! You can choose any one from ['Rock','Paper','Scissor']. Please re-enter your choice : ")
            print("Your choice is : ",userchoice)
        else:
            systemchoice=computeSystemInput()
            print("System's choice is : ",systemchoice)
            computeWinner(userchoice,systemchoice)

if __name__=="__main__":
    play()