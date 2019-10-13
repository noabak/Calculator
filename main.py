print("+++ CALCULATOR +++")
number1= int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
operation=input("Select one arithmetic operation ( / , + , - , x):")
if operation=="/":
    if number2== 0:
        print("In order to realize this operation, the divider must be different to zero !")
    else:
        print(number1,operation,number2,": ",number1/number2)
elif operation=="+":
    print(number1,operation,number2,": ",number1+number2)
elif operation=="-":
    print(number1,operation,number2,": ",number1-number2)
elif operation=="x":
    print(number1,operation,number2,": ",number1*number2)
else:
    print("Invalid operation!")

