import csv

# Ques 1

with open("Assignment_week2/sample.txt", "r") as file:
    content = file.read()
    print(content)


# Ques 2

with open("Assignment_week2/words.txt", "r") as file:
    content = file.read()  

words = content.split()

word_count = len(words)

print("Number of words in the file:", word_count)


# Ques 3

with open("Assignment_week2/output.txt", "w") as file:
    file.write("Hello, Python!")

print("String written to output.txt successfully.")


# Ques 4

import csv

data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]

with open("Assignment_week2/students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("students.csv created successfully.")


# Ques 5 

def read_file_generator(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

file_path = "Assignment_week2/large_file.txt"

for line in read_file_generator(file_path):
    print(line)
