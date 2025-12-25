fruits = ["Mango","Banana","Papaya","Graps","Kiwi"]
new_fruits = [fruits for fruits in fruits if "a" in fruits]
print(new_fruits) 

# Copy a list 
new_fruits = fruits.copy()
print(new_fruits)

new_fruits = fruits + new_fruits
print(new_fruits)