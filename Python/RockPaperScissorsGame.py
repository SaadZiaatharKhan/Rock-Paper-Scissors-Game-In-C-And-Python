import random                   # Imported Random Module
from functools import reduce    # Imported Reduce Function From Functools Module

list_of_statements=["***** welcome to rock, paper, scissor game *****\n","\nLet\'s Start","Enter The Number Of Rounds You Want To Play : ","\nRock, Paper, Scissor\n","Enter Your Option : ","Your Opponent\'s Option : ","You Won !","+1 Points To You\n","You Lose !","+1 Points To Your Opponent\n","Congratulations!\n You Won!","You Lost !","Do You Want To Play Again : Y \ N","Thanks For Playing\n","Hope You Enjoyed\n","Your Total Score Is : ","Your Opponent\'s Total Score Is : ","Tie !","No Points To Anyone\n","\nBetter Luck Next Time\n","No One Wins"] # List Of Statements We Will Be Using In Our Game Is Compiled In The Form Of List So We Don't Have To Type Again And Again
prop=["Rock","Paper","Scissor"] # One Option Will Be Randomly Choosen From This Module
player=[0]    # This List Will Contain Player's Points And Will Be Added At The End
computer=[0]  # This List Will Contain Computer's Points And Will Be Added At The End

print(list_of_statements[0].upper().center(50))
number_of_rounds=int(input(list_of_statements[2])) # Enter The Number Of Rounds You Want To Play

def tie():
  """This Function Deals With What Happens If There Is A Tie Between Player And Computer In A Round"""
  print("\n",list_of_statements[17])
  print(list_of_statements[18]) # No Point Addition In Player Or Computer List As There Is A Tie

def lose():
  """This Function Deals With What Happens If Player Loses And Computer Wins In A Round"""
  print("\n",list_of_statements[8])
  print(list_of_statements[9])
  computer.append(1) # Addition Of 1 As Integer In Computer List As A Point If Player Loses

def won():
  """This Function Deals With What Happens If Player Wins And Computer Loses In A Round"""
  print("\n",list_of_statements[6])
  print(list_of_statements[7])
  player.append(1) # Addition Of 1 As Integer In Computer List As A Point If Player Wins
  
def game():
  """This Is The Main Structure Of Game"""
  
  print(list_of_statements[1].center(50))
  print(list_of_statements[3].center(50))
  opponents_choice=random.choice(prop)    # Using Random Module For Randomly Selecting An Option From Prop List As Computer's Option In Variable opponents_choice
  your_choice=input(list_of_statements[4]) # Your Input From Rock, Paper Or Scissor
  print(list_of_statements[5],opponents_choice)

  if (your_choice=="rock" or your_choice=="Rock" or your_choice=="ROCK"): # If You Choose Rock
    
    if (opponents_choice==prop[0]): # If There Is Rock In Variable opponents_choice
      tie() # Executing Tie Function

    elif (opponents_choice==prop[1]): # If There Is Paper In Variable opponents_choice
      lose() # Executing Lose Function

    else: # If There Is Scissor In Variable opponents_choice
      won() # Executing Won Function

  elif (your_choice=="paper" or your_choice=="Paper" or your_choice=="PAPER"): # If You Choose Paper

    if (opponents_choice==prop[0]): # If There Is Rock In Variable opponents_choice
      won() # Executing Won Function

    elif (opponents_choice==prop[1]): # If There Is Paper In Variable opponents_choice
      tie() # Executing Tie Function

    else:  # If There Is Scissor In Variable opponents_choice
      lose() # Executing Lose Function

  elif (your_choice=="scissor" or your_choice=="Scissor" or your_choice=="SCISSOR"): # If You Choose Scissor

    if (opponents_choice==prop[0]): # If There Is Rock In Variable opponents_choice
      lose() # Executing Lose Function

    elif (opponents_choice==prop[1]):  # If There Is Paper In Variable opponents_choice
      won() # Executing Won Function

    else: # If There Is Scissor In Variable opponents_choice
      tie() # Executing Tie Function

  else: # If Any Other Option Is Chosen Other Than Rock, Paper Or Scissor But A Round Is Lost
    print("\nEnter Any Valid Option")
    print(list_of_statements[18])

def start():
  """From Here Our Game Function Will Start In A Loop Of Number Of Rounds"""
  for i in range (0,number_of_rounds):
    game()

start() # Executing Start Function

player_points=reduce(lambda x,y:x+y, player)     # Adding All The Points Collected In Player List (Collected By Appending) Using Reduce Function
computer_points=reduce(lambda a,b:a+b, computer) # Adding All The Points Collected In Computer List (Collected By Appending) Using Reduce Function

print(list_of_statements[15],player_points)        # Displayig Total Points Of Player
print(list_of_statements[16],computer_points,"\n") # Displayig Total Points Of Computer

if (player_points>computer_points):                # If Player Wins
  print(list_of_statements[10].title().center(50))
  print(list_of_statements[13].title().center(50))
  print(list_of_statements[14].title().center(50))

elif(player_points<computer_points):               # If Player Loses
  print(list_of_statements[11].title().center(50))
  print(list_of_statements[19].title().center(70))
  print(list_of_statements[13].title().center(50))
  print(list_of_statements[14].title().center(50))

else:                                              # If There Is A Tie
  print(list_of_statements[17].title().center(50))
  print(list_of_statements[20].title().center(50))
  print(list_of_statements[19].title().center(50))
  print(list_of_statements[13].title().center(50))
  print(list_of_statements[14].title().center(50))

for_stopping_program_from_immediate_closure_in_shell=input() # For Stopping Program From Immediate Closure In Shell