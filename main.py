# main.py
# Todo: Import operations
from calculatorLab.operations import add, sub, mul, div

def main():
  print("Welcome to the Calculator!")

  #TODO: get user input (float) for two numbers
  a = float(input("Enter the first number: "))
  b = float(input("Enter the second number: "))

  #TODO: ask user for operation
  op = input("Choose operation (+, -, *, /): ")

  #TODO: use if statements to perform the correct operation
  # if op == '+':
    #result = add(a, b)
  #elif op == '-':
    #result = sub(a, b)
  #...
  if op == '+':
     result = add(a,b)
  elif op == '-':
     result = sub( a,b)
  elif op == '*':
     result = mul(a,b)
  elif op == '/':
     result = div(a,b)
  else :
     print("Please try again and enter a valid operation")
     return

  #print the result 
  print("Result: " + str(result))

#running program 
if __name__ == "__main__":
    main()
