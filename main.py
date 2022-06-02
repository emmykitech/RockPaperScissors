import random

print("Welcome to Rock Paper Scissors!")

print("-------------------------------")
print('\nR for rock , P for paper , S for Scissors')


### Set uo variables
cpuScore = 0
playerScore = 0
tieScore = 0
possibleHands = ["R","P","S"]

def checkForWinner(playerHand, computerHand):
    """this function simply accept both users and cpu input"""
    if (playerHand == "R" and computerHand == "P"):
        print("Sorry you lost :(")
        return "Cpu " 

    elif (playerHand == "R" and computerHand == "S"):
        print("Congrats! You won :)")
        return "Player"

    elif (playerHand == "S" and computerHand == "P"):
        print("Congrats! You won")
        return "Player"

    elif(playerHand == "S" and computerHand == "R"):
        print("Sorry, you lost!")
        return "Cpu"

    elif(playerHand == "P" and computerHand == "R"):
        print("Congrats! You win :)")
        return "Player"
  
    elif(playerHand == "P" and computerHand == "S"):
        print("Sorry, you lost!")
        return "Cpu"
    
    else:
        print("It's a tie, play again!")
        return "Tie"

### Start game loop
while(playerScore != 3 and cpuScore != 3):
  ### Validate input
  while True:
    playerHand = input("\nPick a hand: R, P, or S: ")
    if(playerHand == "R" or playerHand == "P" or playerHand == "S"):
      break
    else:
      print("Invalid input. Try again.")
  
  ### Generate computer pick
  computerHand = random.choice(possibleHands)

  ### Print results
  print("Your hand: ", playerHand)
  print("Cpu hand: ", computerHand)
  result = checkForWinner(playerHand, computerHand)

  if(result == "Player"):
    playerScore += 1

  elif(result == "Cpu"):
    cpuScore += 1

  else:
    tieScore += 1
  
  print(f"Your score: {playerScore}, CPU: {cpuScore}, Ties: {tieScore}")

print("Game over! Thank you for playing :)")







