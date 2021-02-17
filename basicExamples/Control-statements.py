x = 10
y = 20
if x > y:
    print('x is greater then y')
else:
    print('y is greater then x')

# ------IF elif example -------#
'''
If marks are >=60, first class
if marks are <60 and >=50, second class
if marks are <50 and >=35, third class
if marks <35, failed 
'''
marks = 34
if marks >= 60:
    print("first class")
elif marks >= 50:
    print("second class")
elif marks >= 35:
    print("third class")
else:
    print("Failed")

# --------while example----- #
data = 1
while data <= 10:
    print(data)
    data = data + 1;

# ----- Continue example------#
print('##### continue example ######')
x = [1, 2, 0, 7, 1.5]
a = 2
for data in x:
    if data == 0:
        continue;
    a = data * a;
print(a);

# -----Break example -----#
print('##### break example ######')
x = [1, 2, 0, 7, 1.5]
a = 2
for data in x:
    if data == 0:
        break;
    a = data * a;
print(a);
