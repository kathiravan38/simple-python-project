#simple arithimatic calculator

operator=input("enter the operator(+,-,*,/):")
if operator in ['+','-','*','/']:
    a=float(input("enter number 1:"))
    b=float(input("enter number 2:"))
    
    if operator == "+":
        result = a+b
        print(f"{a} + {b} = {round(result, 3)}")
    elif operator == "-":
        result = a-b
        print(f"{a} - {b} = {round(result, 3)}")
    elif operator == "*":
        result = a*b
        print(f"{a} * {b} = {round(result, 3)}")
    elif operator == "/":
        if b == 0:
            print("zero division error")
        else:
            result=a/b
            print(f"{a} / {b} = {round(result, 3)}")

else:
    print(f" '{operator}' is not valid \nenter the valid operator(+,-,*,/)")
    

