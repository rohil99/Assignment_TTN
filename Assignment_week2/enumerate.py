# Ques 1

fruits = ["apple", "banana", "cherry"]

for idx, fruit in enumerate(fruits):
    print(idx, fruit)


# Ques 2

person = {"name": "Alice", "age": 30, "city": "New York"}

for i, (k, v) in enumerate(person.items()):
    print(f"{k}: {v}")


# Ques 3

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
l = list()
for idx, fruit in enumerate(fruits, start = 1):
    if idx%2 == 0:
        l.append((idx, fruit))

print(l)