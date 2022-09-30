operation = input("Please input the type of operation (+,-, *, /) ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operation == "+":
  print(f"{num1} + {num2} =", num1 + num2)
elif operation == "-":
  print(f"{num1} - {num2} =", num1 - num2)
elif operation == "*":
  print(f"{num1} * {num2} =", num1 * num2)
elif operation == "/":
  print(f"{num1} / {num2} =", num1 / num2)
else:
  print("Invalid operation input. Please try again")