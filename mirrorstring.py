input_string = input("Enter string : ")
n = int (input("Enter n : "))

# Creating dictionary for mirror operations
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]
dict1 = dict (zip(alphabets,reverse_alphabets))

# Finding the part of the string on which we will do mirror operations
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

# Finding the mirror string 
mirror = ""
for i in range (0,len(suffix)):
    mirror = mirror + dict1[suffix[i]]

# Creating the final string 
res = prefix + mirror
print ("The result is : ",res)