
keep_going = True
menu = "1. Add \n2. Subtract \n3. Divide \n4. Multiply \n5. Quit \n\n Please select an option:"

print("Welcome to the calculator program! \n\n")
print(menu)

choice = int(input())

while choice < 1 or choice > 5:
  print("\n Please choose between 1 and 5.\n\n")
  print(menu)
  choice = int(input())

if choice >= 1 and choice <= 5:
  keep_going = True

while keep_going:
  if choice == 1:
    print("\nAdding \n")
    print("Enter a number:")
    num1 = int(input())
    print("\nEnter a number:")
    num2 = int(input())

    print("\n\nRESULT:\n")
    result = num1 + num2
    print(num1, " + ", num2, " = ", result)
    print("\n")

    print(menu)
    choice = int(input())

  if choice == 2:
    print("\nSubtracting \n")
    print("Enter a number:")
    num1 = int(input())
    print("\nEnter a number:")
    num2 = int(input())

    print("\n\nRESULT:\n")
    result = num1 - num2
    print(num1, " - ", num2, " = ", result)
    print("\n")

    print(menu)
    choice = int(input())

  if choice == 3:
    print("\nDividing \n")
    print("Enter a number:")
    num1 = int(input())
    print("\nEnter a number:")
    num2 = int(input())

    print("\n\nRESULT:\n")
    result = num1 / num2
    print(num1, " / ", num2, " = ", result)
    print("\n")

    print(menu)
    choice = int(input())

  if choice == 4:
    print("\nMultiplying \n")
    print("Enter a number:")
    num1 = int(input())
    print("\nEnter a number:")
    num2 = int(input())

    print("\n\nRESULT:\n")
    result = num1 * num2
    print(num1, " * ", num2, " = ", result)
    print("\n")

    print(menu)
    choice = int(input())

  if choice == 5:
    print("See you next time! Goodbye.")
    keep_going = False
