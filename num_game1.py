import random


random_number = random.randint(1,100)
tries = 0
tries_remaining = 5


while tries < 5:
  guess = input("Guess a random number between 1 and 100. ")
  tries += 1
  tries_remaining -= 1

  try:
    guess_num = int(guess)
  except:
    print("That's not a whole number!")
    break

  if not guess_num > 0 or not guess_num < 101:
    print("That number is not between 1 and 100.")
    break



  elif guess_num == random_number:
    print("Congratulations! You are correct!")
    print("It took you {} tries.".format(tries))
    break


  elif guess_num < random_number:
    if tries_remaining > 0:
      print("I'm sorry, that number is low. You have {} tries remaining.".format(int(tries_remaining)))
      continue
    else:
      print("Sorry, but my number was {}".format(random_number))
      print("You are out of tries. Try again ?.")



  elif guess_num > random_number:
    if tries_remaining > 0:
      print("I'm sorry, that number is high. You have {} tries remaining.".format(int(tries_remaining)))
      continue
    else:
      print("Sorry, but my number was {}".format(random_number))
      print("You are out of tries. Play again sometime.")
