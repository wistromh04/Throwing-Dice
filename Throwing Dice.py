import random

def throwinDice():
    global player1Score, player2Score, player1Money, player2Money
    player1Score = 0
    player2Score = 0
    print("Welcome to Throwin Die!")
    targetScoreCatcher()
    
    while player1Score < desiredScore and player2Score < desiredScore:
        player1Turn()
        if player1Score >= desiredScore:
            print("Player One wins!")
            break
        player2Turn()
        if player2Score >= desiredScore:
            print("Player Two wins!")
            break

#Uses random function to generate a number on a dice 1-6
def roll():
    result = random.randint(1, 6)
    return result 

#Prompts if you want to roll again or end your turn
def continueTurn():
    response = input("Do you want to roll again? (Y/N)")
    return response.upper() == "Y"

def player1Turn():
    global player1Score
    while True:
        numToAdd1 = roll()
        if numToAdd1 == 1:
            player1Score = 0
            print("Player One rolled a 1")
            print("Player One Score is now 0")
            break
        else:
            player1Score += numToAdd1
            print("Player One rolled a " + str(numToAdd1))
            print("Player One Score is now " + str(player1Score))
            if not continueTurn():
                break

def player2Turn():
    global player2Score
    while True:
        numToAdd2 = roll()
        if numToAdd2 == 1:
            player2Score = 0
            print("Player Two rolled a 1")
            print("Player Two Score is now 0")
            break
        else:
            player2Score += numToAdd2
            print("Player Two rolled a " + str(numToAdd2))
            print("Player Two Score is now " + str(player2Score))
            if not continueTurn():
                break

#retrieves the players desired target score & and will continue to do so until player enters an int greater than 0
def targetScoreCatcher():
    global desiredScore
    while True:
        try: 
            desiredScore = int(input("What Target Score you want? "))
            if desiredScore <= 0:
                print("Please enter a positive integer greater than 0.")
            else:
                break  
        except ValueError:
            print("Please enter a valid integer.") 

throwinDice()
