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
    break
  else:
    print("Invalid choice")