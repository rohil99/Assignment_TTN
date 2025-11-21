# Ques 1

strings = ["1", "2", "3", "4", "5"]
numbers = [int(s) for s in strings]
print(numbers)


# Ques 2

numbers = [1, 5, 13, 4, 16, 7]
numbers_filtered = [n for n in numbers if n>10]
print(numbers_filtered)

# Ques 3

n = 5
squared_list = [i*i for i in range(1, n+1)]
print(squared_list)


# Ques 4

matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
flattened_matrix = [i for n in matrix for i in n]
print(flattened_matrix)


# Ques 5

keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)


# Ques 6

scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
new_dict = {}
for key, value in scores.items():
    if value > 80:
        new_dict[key] =  value
print(new_dict)

