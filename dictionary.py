# Creating a dictionary
phones = {
    "John" : 1236547890,
    "Andrews" : 9874563210,
    "Nikhil" : 7879197687
}
# Printing the dictionary
print (phones)

# Checking type of dictionary
print(type(phones))

# Check the length of dictionary
print(len(phones))

# Access items of dictionary
print(phones["Nikhil"])
print(phones.get("Nikhil"))
print(phones.keys())

# Update value in dictionary 
phones ["John"] = 1234567899
print(phones)

# Add elements in a dictionary
phones["Sanju"] = 1236547893
print(phones)

# Adding more dictionary 
more_phones = {
    "Gopal" : 9926535015
}
phones.update(more_phones)
print(phones)

# Remove elements in a dictionary
phones.pop("John")
print(phones)

phones.popitem() # This will remove the last added item
print(phones)

# phones.clear() # This will empty the dictionary
#print(phones)

# Printing elements of dictionary
for x in phones:
    print(x)
    print(phones[x])

for x in phones.items():
    print(x)

for x,y in phones.items():
    print(x,y)

# Nested Dictionary 
phone = {
    "Area1" : {
        "x" : 1,
        "y" : 2,
        "z" : 3
    },
    "Area2" : {
        "a" : 4,
        "b" : 5,
        "c" : 6
    }
}
print(phone["Area1"]["y"])
print(phone["Area2"]["b"])