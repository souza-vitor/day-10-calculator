import art
import replit


def calculate(num1, operation, num2):
  result = 0
  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    result = num1 / num2
  else:
    print("Invalid operation")

  print(f"{num1} {operation} {num2} = {result}")
  return result

def main():

  num1 = int(input("Enter the first number: "))

  repeat = ''
  
  while repeat != 'n':
    print("+")
    print("-")
    print("*")
    print("/")
    operation = input("Select the operation: ")
    num2 = int(input("What's the next number? "))
    
    num1 = calculate(num1, operation, num2)
    
    repeat = input(f"Type 'y' to continue calculating with {num1} or type 'n' to start a new calculation: ")
  
  if repeat == 'n':
    replit.clear()
    main()

print(art.logo)
main()