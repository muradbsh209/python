user_name = input(f"Enter your name: ")
user_age = input(f"Enter your age: ")
user_favnumber = input(f"Enter your name: ")

user_age = int(user_age)
user_favnumber = int(user_favnumber)

future_age = user_age + 10
user_favnumber2 = user_favnumber ** 2

if user_favnumber % 2 == 0:
    flag = "even"
else: flag = "odd"

print(f"Hi {user_name}! In 10 years you'll be {future_age}. Your favorite number squared is {user_favnumber2}, and it's {flag}.")

""" Answer of question:
    The input() captures everything in text format. 
    Python treats different data types differently, so type casting is necessary. 
    Python can not do mathematical operations on data types like as string or boolean, so they should be converted into numeric format like as integer or float."""