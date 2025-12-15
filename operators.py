# Arithmetic Operators 
print ("Sum : ", 4+3)
print ("Substraction : ",4-3)
print ("Division : ",4/3)
print ("Multiplicartion : ",4*3)
print ("Modulus : ",4%3)
print ("Floor Division : ",4//3)
print ("Exponentiation :",4**3)
print("\n")

# Assignment Operator 
n1=5
n2=n1
print(n1,n2)
print("\n")

n2+=n1
print (n1,n2)
print("\n")

# Comparison Operators
n1=5
n2=3
print (n1>n2)
print("\n")
print (n1<n2)
print("\n")

# Logical Operators.
exp1 = 22>11
exp2 = 44>55
print("Exp1 and Exp2 is while using (and) operator : ",exp1 and exp2)
print("Exp1 and Exp2 is while using (or) operator : ",exp1 or exp2)
print("Not Exp1 : ",not(exp1))
print ("\n")

# Identifty Operator 
x=3
y=3
print("If x is y : ",x is y)
print("If x is not y : ",x is not  y)
print ("\n")

# Membership Operators
fruits = ["apples", "banana", "cherry"]
print("If Banana is present in fruits : ","banana" in fruits )
print("If Mango is not present in fruits : ","mango" not in fruits )
print ("\n")

# Bitwise Operators
a=5
b=3
print("A and B :", a & b)
print("A or B :", a | b)
print("A xor B :", a ^ b)