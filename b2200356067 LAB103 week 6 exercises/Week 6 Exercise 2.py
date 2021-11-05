email = input("Please enter your email: ")
list1 = list(email)
a = 0
b = 0
for i in list1:
    if i == '@':
     a = 1

for i in list1:
    if i == '.':
        b = 1

if a == 1 and b == 1:
    print("Your email is correct.")
else:
    print("Your email is not correct")