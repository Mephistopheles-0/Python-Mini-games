import random

def guessing_game(type):
  """
  This function plays a guessing game with the user.

  Args:
    type: The type of game to play. Can be "animals" or "numbers".

  Returns:
    None.
  """

  # Generate a random number or object, depending on the game type.
  if type == "animals":
    animals = ["dog", "cat", "bird", "fish", "horse"]
    random_animal = random.choice(animals)
  elif type == "numbers":
    random_number = random.randint(1, 100)

  # Get the user's guess.
  user_guess = input("What is your guess? ")

  # Check if the user's guess is correct.
  if type == "animals":
    if user_guess == random_animal:
      print("Correct!")
    else:
      print("Incorrect. The correct answer was {}.".format(random_animal))
  elif type == "numbers":
    if int(user_guess) == random_number:
      print("Correct!")
    else:
      print("Incorrect. The correct answer was {}.".format(random_number))


def main():
  # Get the user's choice of game.
  game_type = input("What type of game would you like to play? (animals, numbers) ")

  # Play the game.
  guessing_game(game_type)


if __name__ == "__main__":
  main()
