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
    break
  else:
    print("Invalid choice")