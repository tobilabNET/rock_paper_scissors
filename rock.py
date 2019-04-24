#rock paper scissor game
import random
player_score = 0
computer_score = 0
while True:
    print("rock, paper or scissors?")
    player = str(input())
    player = player.lower()
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    print("You chose ", player)
    print("Computer chose ",computer)
    if player == "rock" and computer == "rock":
        print("It's a tie")
        print("score is ", player_score, ":", computer_score )            
    elif player == "rock" and computer=="paper":
        print("You lose!")
        computer_score+= 1
        print("score is ", player_score, ":", computer_score )
    elif player == "rock" and computer=="scissors":
        print("You win!")
        player_score+= 1
        print("score is ", player_score, ":", computer_score )
    elif player == "paper" and computer== "paper":
        print("It's a tie")
        print("score is ", player_score, ":", computer_score )
    elif player == "paper" and computer== "scissors":
        print("You lose")
        computer_score+= 1
        print("score is ", player_score, ":", computer_score )
    elif player == "paper" and computer== "rock":
        print("You win")
        player_score+= 1
        print("score is ", player_score, ":", computer_score )  
    elif player == "scissors" and computer== "scissors":
        print("It's a tie")
        print("score is ", player_score, ":", computer_score )
    elif player == "scissors" and computer== "rock":
        print("You lose")
        computer_score+= 1
    elif player == "scissors" and computer == "paper":
        print("You win")
        player_score+= 1
        print("score is ", player_score, ":", computer_score )
    else: 
        print("Invalid input, please chose again")
