#Task 1

marks = int(input(f"Enter your an exam mark(out of 100): "))
if 100 >= marks >= 91:
    print(f'A')
elif marks >= 81 :
    print(f'B')
elif marks >= 71:
    print(f'C')
elif marks >= 61:
    print(f'D')
elif marks >= 51:
    print(f'E')
else:
    print(f'f')