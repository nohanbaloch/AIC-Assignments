
def calculator(num1, op, num2):

    while True:
      try:      
        op=input("enter operation + , - , * , / .").strip()
        num1=float(input("enter a first number"))
        num2=float(input("enter a second number"))
        break
      except:
          print("Invalid input") 

    
    if op == "+":
        result=num1+num2

    elif op == "-":
        result=num1-num2

    elif op == "*":
        result=num1*num2

    elif op == "/":
        result=num1/num2
    else:
        print("Error!")
    
    return result
result = calculator(num1, op, num2)
print("the result is: ", result)
