import random
import time

print("Welcome to Rock, Paper, Scissors Game!\n") #greeting message



while True: # Reaplay loop!

    while True: # Game loop!
        computer_choice = random.choice(["rock", "paper", "scissors"]) # the computer's choice is randomly selected!

        User_choice = input("ENTER YOUR CHOICE (rock, paper, scissors): ") # user's input for choice
        User_choice = User_choice.lower() # lowering the user's input to make it case insensitive!

        # Validating the user's input and determining the winner of the game!
        if User_choice not in ["rock", "paper", "scissors"]: #if the user's input is not valid, it will ask them to enter a valid choice and continue the loop!
            print("Sorry Bruh, that ain't a valid choice! just enter rock, paper, or scissors!!")
            continue        
        if User_choice == computer_choice: # if tie!
            print("hmmm... i am thinking...")
            time.sleep(2)
            print("I think i know!")
            time.sleep(1)
            print(f"oh you chose? : {User_choice}")

            print(f"lets go again, I will win this time!!, BTW I chose: {computer_choice}")
            continue

        # if the user wins!
        elif (User_choice == "rock" and computer_choice == "scissors") or (User_choice == "paper" and computer_choice == "rock") or (User_choice == "scissors" and computer_choice == "paper"):
            
            print("hmmm... i am thinking...")
            time.sleep(2)
            print("I think i know!")
            time.sleep(1)
            print(f"oh you chose? : {User_choice}")
            
            print(f"Congrats, you win!!\n My choice was: {computer_choice}")
            break

        #if the bot wins!
        elif (User_choice == "rock" and computer_choice == "paper") or (User_choice == "paper" and computer_choice == "scissors") or (User_choice == "scissors" and computer_choice == "rock"):
            print("hmmm... i am thinking...")
            time.sleep(2)
            print("I think i know!")
            time.sleep(1)
            print(f"oh you chose? : {User_choice}")

            print(f"I win!! Better luck next time!!\n My choice was: {computer_choice}")
            break
        
        # game loop ends here!
    # the replay loop's code starts here!
    replay = input("wanna play agian? (y/n):") # asking
    # IF user enters NO!
    if replay.lower() != "y" and replay.lower() != "yes":
        print("\n")
        print("Thanks for playing Rock, Paper, Scissors! See you next time!\n")
        break
    # IF user enters YES!
    elif replay.lower() == "y" or replay.lower() == "yes":
        print("\n")
        continue

    else:
        print("your weird...")
        time.sleep(1)
        print("cuz u cant type duh!")
        time.sleep(1)
        print("k love u byee <3")
        time.sleep(3)
        break