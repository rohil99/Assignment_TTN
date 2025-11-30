# Ques 1

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()

for _ in range(10):
    print(next(fib_gen))


# Ques 2

def infinite_multiples(n):
    i = 1
    while True:
        yield n * i
        i += 1

n = 3
multiple_gen = infinite_multiples(n)

for _ in range(5):
    print(next(multiple_gen))


# Ques 3

def repeat_word(word, times):
    for _ in range(times):
        yield word


word = "hello"
times = 5

gen = repeat_word(word, times)

for w in gen:
    print(w)

