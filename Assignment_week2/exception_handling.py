# Ques 1

a= 10
b=0

try:
    res = a/b
    print("result is ", res)
except ZeroDivisionError as e:
    print("Error- ",e)


# Ques 2

my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError as e:
    print("Error- ",e)


# Ques 3

def safe_divide(a,b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print("Error- ",e)
    except TypeError as e:
        print("Error- ",e)
    finally:
        print("Execution completed")

safe_divide(1,0)
safe_divide(1,"a")
