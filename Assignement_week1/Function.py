# Ques 1

def calculate_area(length, width = 10):
    return length * width

print(calculate_area(10, 5))
print(calculate_area(10))


# Ques 2

def calculate_factorial(num):
    if (num == 0 | 1):
        return num
    else:
        return num * calculate_factorial(num-1)
    
print(calculate_factorial(9))

# Ques 3

reversed_str = ""
def reverse_string(string):
    reversed_str = string[ : : -1]
    return reversed_str

print(reverse_string("hello"))


# Ques 4
s = 0
def sum_of_lists(l1, l2):
    s = sum(l1) + sum(l2)
    return s

a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1] 
print(sum_of_lists(a, b))


# Ques 5

def distnct_sorted(l1):
    # l1.distinct()
    l1 = list(set(l1))
    l1.sort()
    return l1

a = [4,1,2,3,3,1,3,4,5,1,7]
print(distnct_sorted(a))

