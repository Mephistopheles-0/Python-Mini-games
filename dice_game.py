import random

def roll_dice():
  """
  This function rolls two dice and returns the sum of the rolls.

  Returns:
    The sum of the rolls.
  """

  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)

  return dice1 + dice2

def guess_sum():
  """
  This function gets the user's guess for the sum of the next roll of two dice.

  Returns:
    The user's guess.
  """

  guess = input("What is your guess for the sum of the next roll? ")

  return int(guess)

def main():
  """
  This function plays the dice game.
  """

  # Initialize the game state.
  player_score = 0
  computer_score = 0

  # Play the game until one player has won 10 rounds.
  while player_score < 10 and computer_score < 10:

    # Roll the dice.
    dice_sum = roll_dice()

    # Get the user's guess.
    guess = guess_sum()

    # Check if the user's guess is correct.
    if guess == dice_sum:
      player_score += 1
    else:
      computer_score += 1

  # Print the final score.
  print("The final score is:")
  print("Player: {} Computer: {}".format(player_score, computer_score))

  # Determine the winner.
  if player_score > computer_score:
    print("Congratulations! You won the game!")
  else:
    print("The computer won the game. Better luck next time!")


if __name__ == "__main__":
  main()
