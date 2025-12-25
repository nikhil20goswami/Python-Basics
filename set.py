# Creating a sets.
names = {"Nikhil","Tushar",'KP'}

# Print set 
print(names)

# Check length of set.
print(len(names))

# Check data type of set
print(type(names))

# Accessing items of a set 
for x in names :
    print(x)

# Check if an items exust in a set 
if "Nikhil" in names:
    print("Nikhil is in the set")

# Add elements in a set.
names.add("Gopal")
print(names)

# Add another sequence in a set
names_list = ["Maneesh","Lucky"]
names.update(names_list)
print(names)

# Removing elements from a set
names.remove("Maneesh")
#names.discard("Jitesh") # This function willnot throw an error if value is not present in the set.
print(names)

# Joining 2 set 
s1 = {'a','b','c'}
s2 = {'d','e','a'}
print(s1,s2)

s3 = s1.union(s2)
print (s3)

s1.update(s2)
print(s1)

# Keep only duplicates while joining
s1.intersection_update(s2)
print(s1)

# Keep all values except duplicates 
s1.symmetric_difference_update(s2)
print(s1)

