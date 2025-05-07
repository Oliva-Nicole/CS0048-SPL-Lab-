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
  choice = menu()
  if choice == 1:
    subject = input("Enter the subject: ")
    score = float(input("Enter the score: "))
    add_score(subject, score)
  elif choice == 2:
    calculate_average()
  elif choice == 3:
    break
  else:
    print("Invalid choice")