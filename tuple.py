# Creating a tuple.
colours = ("blue","green","red","pink")
print(colours)

# Creating a tuple with 1 item.
fruits = ("apple",)
fruit = ("apple")

# Check type of tuple 
print(type(fruits))
print(type(colours))
print(type(fruit))

# Check length of the tuple.
print(len(fruits))
print(len(colours))
print(len(fruit))
 
# Accessing items in tuple.
print(colours[0]) # positive indexing
print(colours[-2]) # negative indexing
print(colours[0:3]) # range indexing
print(colours[-1:-3]) # negative range indexing 

# Check if an item exist in tuple.
if "blue" in colours:
    print("Blue is present in colours.")

# Traverse the tuple.
for i in colours:
    print(i)

# Concatenate two tuples.
new_colours = ("yellow","brown")
colours = colours + new_colours
print(colours)

# Unpacking a tuple.
colour1, colour2, colour3, colour4, colour5, colour6 = colours
print(colour1, colour2, colour3, colour4, colour5, colour6 )