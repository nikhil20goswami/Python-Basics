n1 = int (input("Enter number 1 : "))
n2 = int (input("Enter number 2 : "))
n3 = int (input("Enter number 3 : "))

if n1>n2:
    if n1>n3:
        print(n1,"(n1) is the greatest")
    else:
        print(n3,"(n3) is the greatest")

else:
    if n2>n3:
        print(n2,"(n2) is the greatest")
    else:
        print(n3,"(n3) is the greatest")