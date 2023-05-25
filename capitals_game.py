import random

def get_capitals():

  countries = requests.get("https://api.worldbank.org/v2/country/all?format=json").json()

  capitals = requests.get("https://www.cia.gov/library/publications/the-world-factbook/fields/2128.html").json()

  capitals_dict = {}
  for country in countries:
    capitals_dict[country["name"]] = capitals[country["iso2c"]]

  return capitals_dict

def play_game():
  capitals_dict = get_capitals()

  correct_answers = 0
  incorrect_answers = 0
  for _ in range(10):
    country = random.choice(list(capitals_dict.keys()))
    guess = input("What is the capital of {}? ".format(country))
    if guess == capitals_dict[country]:
      correct_answers += 1
    else:
      incorrect_answers += 1

  print("Your final score is:")
  print("Correct answers: {} Incorrect answers: {}".format(correct_answers, incorrect_answers))

  if correct_answers > incorrect_answers:
    print("Congratulations! You won the game!")
  else:
    print("You lost the game. Better luck next time!")


if __name__ == "__main__":
  play_game()
