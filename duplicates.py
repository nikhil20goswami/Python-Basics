l1 = [1,5,5,4]
l2 = [1,2,3,5]
l3 = [1,4,5,8]

# Type casting using sets
s1 = set(l1)
s2 = set(l2)
s3 = set(l3)

# Join using intersection
s1s2 = s1.intersection(s2)
final_set = s1s2.intersection (s3)

final_list = (list(final_set))
print(final_list)