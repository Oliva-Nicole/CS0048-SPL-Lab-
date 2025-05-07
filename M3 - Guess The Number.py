import random
def attempt_counter():
    global attempts
    attempts += 1
    return attempts
    while True:
      guess = int(input("Guess the number: "))
      if guess < number:
        print("Too low!")
        attempt_counter()
      elif guess > number:
        print("Too high!")
        attempt_counter()
      else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")

def guess_the_num():
    number = random.randint(1, 100)
    attempt = 0

def menu():
    print("\nNumber Guessing Game Menu:")
    print("1. Play Game")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ")
    return choice

while True:
    choice = menu()
    if choice == '1':
        guessing_game()
    elif choice == '2':
        print("Exiting the game.")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")