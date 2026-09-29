#Task 2

num = int(input("Enter a number: "))
summa = 0
count = 0

for i in range(1,num+1):

    if i % 3 == 0 and i % 5 == 0:
        print("3 5")
    elif i % 3 == 0:
        print("3")
    elif i % 5 == 0:
        print("5")
    else:
        print(i)

    if i % 2 == 0:
        summa += i
    if i % 3 == 0:
        count += 1

print(f"Sum of all even numbers from 1 to n: {summa}")
print(f"Count of numbers divisible by 3: {count}")