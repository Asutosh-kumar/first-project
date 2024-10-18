#Calculator in which we can perform any thing we can do in a regular calculator#
def add(x, y):
      return x + y
def subtract(x, y):
      return x - y
def multiply(x, y):
      return x * y
def power(x, y):
      if x<0:
            return "invalid input too"
      else:
            return x ** y
def divide(x, y):
      if y==0:
            return "cannot devide zero. invalid input"
      else:
            return x / y
try:
      def calculator():
            while True:
                  print("options")
                  i = ["add", "subtract", "multiply", "divide", "power", "quit"]
                  print(i)
                  print("  |+|", "     |-|", "        |x|", "       |/|", "     |x^y|", "    |q|")
                  options = input(":==> ")
                  if options == "quit" or options == "q":
                        break
                  elif options in ("add", "subtract", "multiply", "divide", "power", "+", "-", "*", "/", "x^y", "q"):
                        n1 = float(input("Enter first number: "))
                        n2 = float(input("Enter second number: "))
                        
                        if options == "add" or options == "+":
                              print("the Sum of these two numbers is: ==>", add(n1,n2))
                        if options == "subtract" or options == "-":
                              print("the Substraction of these two numbers is: ==>", subtract(n1,n2))
                        if options == "multiply" or options == "*":
                              print("the Multiplication of these two numbers is: ==>", multiply(n1,n2))
                        if options == "divide" or options == "/":
                            if n2 == 0:
                                print("invalid input")
                            else:
                              print("the Division of these two numbers is: ==>", divide(n1,n2))
                        if options == "power" or options == "x^y":
                            if n1 < 0:
                                print("invalid input")
                            else:
                              print(n1, "to the power",n2, "is:==>", power(n1,n2))
                  else:
                        print("Recheck the options first _^_")
      calculator()
except Exception as e:
      print(e)
print(calculator())