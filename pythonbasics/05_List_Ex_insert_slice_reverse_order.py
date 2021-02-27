# ---List Example --- #
data = [1, 4, 'A', 10.4]
print(data)
y = [data, 1, 2, 3]
print(y[data[0]])

# ---- Insert at specific index, delete, for loop on list ---- #
x = ['A', 1, 3.4, 'B', 'Python']
print(x)
x.insert(0, "Java")
del data[0]
for data in x:
    print(data)

# ---- slicing in list ---- Print String array in reverse order #
x = [1, 3, 5, 'A', 'B', 12.5]
print(x[::-1])
