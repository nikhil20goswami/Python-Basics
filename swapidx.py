n = int (input("Enter size of list :"))

list = []
for _ in range (n):
    num = int(input())
    list.append(num)

idx1 = int (input("Enter index1 :"))
idx2 = int (input("Enter index2 :")) 
print(list)

# Swapping values at id1 and idx2
temp = list[idx2]
list[idx2] = list[idx1]
list[idx1] = temp

print(list)