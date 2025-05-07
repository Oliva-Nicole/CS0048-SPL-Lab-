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
    break
  else:
    print("Invalid choice")