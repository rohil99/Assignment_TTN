# Ques 1

# num1 = int(input("Enter number to check if it is even or odd: "))
# if(num1 % 2 == 0):
#     print(f"the given number is even")
# else:
#         print(f"the given number is odd")


# Ques 2

s1 = "civic"
reverse_s1 = ""
for i in range(len(s1)-1, -1, -1):
      reverse_s1+=s1[i]
print(reverse_s1)
if(s1 == reverse_s1):
      print(s1, " is a palindrome")
else:
      print(s1, " is not a palindrome")

s2 = "hello"
reverse_s2 = ""
for i in range(len(s2)-1, -1, -1):
      reverse_s2+=s2[i]
print(reverse_s2)
if(s2 == reverse_s2):
      print(s2, " is a palindrome")
else:
      print(s2, " is not a palindrome")


# Ques 3

# n = int(input("Enter a number to generate a fibonacci sequence: "))
# fibonacci_list = list()
# n1 , n2 = 0 , 1
# for i in range(n):
#       fibonacci_list.append(n1)
#       n1 , n2 = n2 , n1+n2
# print(fibonacci_list)


# Ques 4

l = [1,2,3,4,5]
for i in range(len(l)):
      for j in range(i+1, len(l)):
            if (l[i] + l[j] ==9):
                  print([l[i], l[j]])


# Ques 5

n = 1
result_list = list()
while(n <= 20):
      if (n % 2) == 0:
            result_list.append(n)
      n += 1
print(result_list)


# Ques 6

numbers = [10, 20, 30, 40, 50]
search_for = 30
for i in range(len(numbers)):
      if numbers[i] == search_for:
            print(f'{search_for} first occurence found at index {i}')
            break
      

# Ques 7

rng = 10
result_list = list()
for i in range(1, rng+1):
      if i % 2 == 0:
            continue
      else:
            result_list.append(i)
print(result_list)


# Ques 8

# Answer for question 8 is:

# 0
# 1
# 2
# 3
# 4

# as pass statement doesn't effect the flow of the loop


# Ques 9

day = input("Enter a day of the week: ")
day = day.lower()

match day:
      case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            print(f'{day} is a weekday')
      case "saturday" | "sunday":
            print(f'{day} is a weekend')
      case _:
            print("please enter a valid day")

