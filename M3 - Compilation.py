def main_menu():
  print("1. Simple Calculator")
  print("2. Temperature Converter")
  print("3. To-Do List")
  print("4. Number Guessing Game")
  print("5. Student Grade Calculator")
  print("6. Exit")
  return int(input("Enter your choice(1-6): "))

def simple_calculator():
  def menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("6. Exit")
    return int(input("Enter your choice: "))

  def add(x, y):
    sum = x + y
    print("Sum:",sum)

  def subtract(x, y):
    difference = x - y
    print("Difference:",difference)

  def multiply(x, y):
    product = x * y
    print("Product:",product)

  def divide(x, y):
    if y==0:
      print("Cannot divide by zero")
    else:
      quotient = x / y
      print("Quotient:",quotient)

  def modulo(x, y):
    remainder = x % y
    print("Modulo:",remainder)

  while True:
    print("Simple Calculator")
    choice = menu()
    if choice == 1:
      x = int(input("Enter first number: "))
      y = int(input("Enter second number: "))
      add(x,y)
    elif choice == 2:
      x = int(input("Enter first number: "))
      y = int(input("Enter second number: "))
      subtract(x,y)
    elif choice == 3:
      x = int(input("Enter first number: "))
      y = int(input("Enter second number: "))
      multiply(x,y)
    elif choice == 4:
      x = int(input("Enter first number: "))
      y = int(input("Enter second number: "))
      divide(x,y)
    elif choice == 5:
      x = int(input("Enter first number: "))
      y = int(input("Enter second number: "))
      modulo(x,y)
    elif choice == 6:
      print("Exitiing calculator...")
      print("----------------------")
      break
    else:
      print("Invalid choice")

def temperature_converter():
  def menu():
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Convert Celcius to Kelvin")
    print("4. Exit")
    return int(input("Enter your choice(1-4): "))

  def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature: ",fahrenheit, "°F")

  def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature: ",celsius, "°C")

  def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    print("Temperature: ",kelvin, "°K")

  while True:
    print("Temperature Converter")
    choice = menu()
    if choice == 1:
      celsius = float(input("Enter temperature in Celsius: "))
      celsius_to_fahrenheit(celsius)
    elif choice == 2:
      fahrenheit = float(input("Enter temperature in Fahrenheit: "))
      fahrenheit_to_celsius(fahrenheit)
    elif choice == 3:
      celsius = float(input("Enter temperature in Celsius: "))
      celsius_to_kelvin(celsius)
    elif choice == 4:
      print("Exiting temperature converter...")
      print("---------------------------------")
      break
    else:
      print("Invalid choice")

def to_do_list():
  def increase_counter():
    global counter
    counter += 1
    return counter

  def decrease_counter():
    global counter
    counter -= 1
    return counter

  def menu():
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
    return int(input("Enter your choice(1-4): "))

  def add_task(task):
    tasks.append(task)
    increase_counter()
    print("Task added! Number of Tasks: ", counter)

  def remove_task(task):
    if task in tasks:
      tasks.remove(task)
      decrease_counter()
      print("Task removed! Number of Tasks: ", counter)
    else:
      print("Task not found")

  def view_tasks():
    print("Number of Tasks: ", counter)
    for task in tasks:
      print(task)

  tasks = []
  counter = 0
  while True:
    print("To-Do List")
    choice = menu()
    if choice == 1:
      task = input("Enter the task to add: ")
      add_task(task)
    elif choice == 2:
      task = input("Enter the task to remove: ")
      remove_task(task)
    elif choice == 3:
      view_tasks()
    elif choice == 4:
      print("Exiting to-do list...")
      print("-----------------------")
      break
    else:
      print("Invalid choice")

def guessing_game():
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
    print("Number Guessing Game")
    choice = menu()
    if choice == '1':
        guessing_game()
    elif choice == '2':
        print("Exiting the game.")
        print("--------------------")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")

def student_grade_calculator():
  grade = []

  def menu():
    print("1. Add Score")
    print("2. Calculate Average")
    print("3. Exit")
    return int(input("Enter your choice(1-3): "))

  def add_score(subject, score):
    grade.append((subject, score))
    print("Score added!")

  def calculate_average():
    total = 0
    for _, score in grade:
      total += score
    average = total / len(grade)
    print("Average Grade: ", average)

  while True:
    print("Student Grade Calculator")
    choice = menu()
    if choice == 1:
      subject = input("Enter the subject: ")
      score = float(input("Enter the score: "))
      add_score(subject, score)
    elif choice == 2:
      calculate_average()
    elif choice == 3:
      print("Exiting student grade calculator...")
      print("-----------------------------------")
      break
    else:
      print("Invalid choice")

while True:
  choice = main_menu()
  if choice == 1:
    simple_calculator()
  elif choice == 2:
    temperature_converter()
  elif choice == 3:
    to_do_list()
  elif choice == 4:
    guessing_game()
  elif choice == 5:
    student_grade_calculator()
  elif choice == 6:
    print("Closing program...")
    break
  else:
    print("Invalid choice")