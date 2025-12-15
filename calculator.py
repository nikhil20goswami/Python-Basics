num1 = int (input("Enter number 1 : "))
num2 = int (input("Enter number 2 : "))

operator = input("Enter Operator : ")

match operator:
    case"+":
        print ("Sum is :",num1+num2)
    
    case"-":
        print ("Substraction is :",num1-num2)

    case"*":
        print ("Multiplication is :",num1*num2)

    case"/":
        print ("Division is :",num1/num2)

    case _:
        print ("Enter a Valid Operator")


