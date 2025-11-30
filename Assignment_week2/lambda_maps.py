from functools import reduce

# Ques 1

a = [1, 2, 3, 4]
double_list = list(map(lambda x: x*2, a))
print(double_list)


# Ques 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x: x%2==0, numbers))
print(even_list)


# Ques 3

words = ["apple", "banana", "cherry", "date"]
longest_word = reduce(lambda acc, x : x if len(x)> len(acc) else acc, words)
print(longest_word)


# Ques 4

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
square_floats = list(map(lambda x: round(x**2, 1), my_floats))
print(square_floats)


# Ques 5

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
filtered_names = list(filter(lambda x: len(x)<=7 , my_names))
print(filtered_names)


# Ques 6

l = [1, 2, 3, 4, 5]
sum_list = reduce(lambda acc, x: acc+x, l)
print(sum_list)
