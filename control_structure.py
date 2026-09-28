#Grading System

marks = int(input(f"Enter your an exam mark(out of 100): "))
if 0 <= marks <= 100:
    if marks >= 90:
        print(f'Your grade is A')
    elif marks >= 75:
        print(f'Your grade is B')
    elif marks >= 50:
        print(f'Your grade is C')
    else:
        print(f'Your grade is F')

else: print(f"Input your score between 0 and 100.")

###########################################################

#Multiplication Table

print()
number = int(input(f"Enter a number: "))

for i in range(1,11):
    print(f"{number} x {i} = {number * i}")

################################################################

#Password Retry System

print()
correct_passw = "2026 Murad is learning PL"
input_passw = ""
attempts = 0

while correct_passw != input_passw:
    input_passw = input(f"Enter a password: ")
    attempts += 1
    if correct_passw == input_passw:
        print(f"You have logged in successfully")
    if attempts == 3:
        print(f"You had a maximum of 3 attempts")
        break