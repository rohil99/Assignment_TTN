# Ques 1

numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
print(f'minimum number in this list is {min(numbers)}')
print(f'maximum number in this list is {max(numbers)}')


# Ques 2

setn = {5, 10, 3, 15, 2, 20}
print(f'minimum number in this set is {min(setn)}')
print(f'maximum number in this set is {max(setn)}')


# Ques 3

def shortest_longest(wordsStr):
    shortest = min(wordsStr, key=len)
    longest = max(wordsStr, key=len)
    return (shortest, longest)

words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
print(shortest_longest(words))
