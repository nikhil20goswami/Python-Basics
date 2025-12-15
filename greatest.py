n1 = int (input("Enter number 1 : "))
n2 = int (input("Enter number 2 : "))
n3 = int (input("Enter number 3 : "))

if n1>n2 and n1>n3:
    print(n1,"(n1) is greatest")

elif n2>n1 and n2>n3:
    print(n2,"(n2) is greatest")

else:
    print(n3,"(n3) is greatest")