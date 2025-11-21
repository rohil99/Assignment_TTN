# Ques 1

name = input("What is your name? ")
greeting_message = f'Hello {name}. Welcome to Python training'
print(greeting_message)


# Ques 2

n1 = int(input("Please enter the number 1: "))
n2 = int(input("Please enter the number 2: "))
print("the sum of the two numbers is: " + str(n1+n2))
print("the multiplication of two number is: " + str(n1*n2))
print("the diviosn of two number is: " + str(n1/n2))


# Ques 3

names = input("Please enter comma separated names: ")
names = names.split(",")
print(names)

# Ques 4

age = int(input("please enter your age: "))
if (age >= 18 ):
    print("You are eligible to vote")

else:
    print("You are NOT eligible to vote")


# Ques 5

value = 3.14159
print(f"{value:.2f}")