n = int(input("Please enter your number: "))
total1 = 0
total2 = 0
a = 0
for i in range (0,n+1):
    if i % 2 != 0:
        total1 += i
    elif i % 2 == 0:
        a += 1
        total2 += i
        total2 = total2/a
print("Odd number total: ", total1)
print("Even number total: ", total2)