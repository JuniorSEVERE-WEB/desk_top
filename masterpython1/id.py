lst1 = [1, 2]
lst2 = lst1
print("lst1 id:", id(lst1))
print("lst2 id:", id(lst2))

lst2 += [3]
print("lst1:", lst1)
print("lst2:", lst2)
print("lst1 id:", id(lst1))
print("lst2 id:", id(lst2))
