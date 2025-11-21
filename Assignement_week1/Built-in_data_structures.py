# Ques 1

nums = [1, 2, 3, 4, 5]
print(f"from the given list {nums}, the maximun value is {max(nums)} and the minimun value is {min(nums)}" )

# Ques 2

a = [1,2,3,4]      
b = [5,6,7,8] 
a.extend(b)
print(a)


# Ques 3

a = [1,3,4,5,2,1,3,9,3]
print(a.count(3))


# Ques 4

a = [1,3,4,5,2,1,3,9,3]
a.sort()
print(a)

# Ques 5

numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(numbers)

# Ques 6 

numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print(numbers)

# Ques 7

set1 = {1, 2, 3}    
set2 = {3, 4, 5}
set3 = set1.intersection(set2)
print(set3)

# Ques 8 

fruits = ('apple', 'banana', 'apple', 'cherry')
print(f"the count of 'apple' in 'fruits' tuple is {fruits.count('apple')}")

# Ques 9 

tuple1 = (1, 2, 3)     
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)

# Ques 10

person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"the value of age is {person.get('age')}")


# Ques 11 

person = {"name": "Alice", "age": 30, "city": "New York"}
person["gender"] = "M"
print(person)

# Ques 12

person = {"name": "Alice", "age": 30, "city": "New York"}
del person["city"]
print(person)


# Ques 13

dict1 = {"a": 1, "b": 2}   
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)



