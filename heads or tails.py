import random

def continuing():
  contnue = input("Do you want to continue? Y/N ").lower()
  if contnue == "y":
    return True
  elif contnue == "n":
    print("Have a nice day!")
    contnue = False
    return False
  else:
    print("Type Y or N!")
    return continuing()
contnue = True
score = 0
while contnue == True:
  coin = random.randint(1, 2)
  #heads = 1
  #tails = 2
  guess = input(f"Heads or tails? ").lower()
  if guess == "heads" and coin == 1 or guess == "tails" and coin == 2:
    print("Correct!")
    score += 1
    print(f"Your score: {score}")
    if not continuing():
      break
  elif guess == "heads" and coin == 2 or guess == "tails" and coin == 1:
    print("Better luck next time!")
    print(f"Your score: {score}")
    if not continuing():
      break
  else:
    print("You have to type \"heads\" or \"tails\"!")
    continue
