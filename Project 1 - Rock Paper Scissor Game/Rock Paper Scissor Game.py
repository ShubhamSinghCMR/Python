"""
Rock Paper Scissors Game
"""
import random
move_lst=['Rock','Paper','Scissor']
player_name=input("Welcome to this game. Please enter your name: ")
player_choice=None
CPU_choice=None
winner=None
choice=None
while True:
    print(f"{player_name}, enter your choice:\nPress 1 for Rock\nPress 2 for Paper\nPress 3 for Scissor:")
    while True:
        choice=int(input())
        if choice==1:
            player_choice="Rock"
        elif choice==2:
            player_choice="Paper"
        elif choice==3:
            player_choice="Scissor"
        
        if choice ==1 or choice==2 or choice ==3:
            break
        else:
            print("Please enter correct choice!")
    CPU_choice=random.choice(move_lst)
    print(f"CPU choice: {CPU_choice}")
    print(f"Your choice: {player_choice}\n")
    if CPU_choice==player_choice:
        print("You TIED!!!")
        continue
    elif CPU_choice=="Rock":
        if player_choice=="Scissor":
            winner="CPU"
        elif player_choice=="Paper":
            winner=player_name
    elif CPU_choice=="Paper":
        if player_choice=="Scissor":
            winner=player_name
        elif player_choice=="Rock":
            winner="CPU"
    elif CPU_choice=="Scissor":
        if player_choice=="Rock":
            winner=player_name
        elif player_choice=="Paper":
            winner="CPU"
    if winner is not None:    
        print (f"\nWinner is {winner} \nThank you for playing!\n\n")
        stat=input("To continue playing, press 'c' or to exit press 'e'")
        if stat.lower()=='c':
            continue
        elif stat=='e':
            break
    