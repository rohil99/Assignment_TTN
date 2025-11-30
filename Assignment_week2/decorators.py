import time

# Ques 1

def time_func(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Start Time: {start}")
        print(f"End Time: {end}")
        print(f"Total Time Taken: {end - start} seconds")
        return result
    return wrapper

@time_func
def append_numbers():
    num_list = list()
    for i in range(1, 1001):
        num_list.append(i)

append_numbers()


# Ques 2

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i} failed with error: {e}")
                    if i == times:
                        print("All retries failed.")
        return wrapper
    return decorator


@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")



# Ques 3

def validate_positive(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be a positive number.")
        return func(x)
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5


# Ques 4

def cache(func):
    cache_result = {}
    
    def wrapper(x):
        if x in cache_result:
            print("Returning cached result")
            return cache_result[x]
        
        result = func(x)
        cache_result[x] = result
        return result

    return wrapper

@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x
	
expensive_computation(5)
expensive_computation(5)


# Ques 5

def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if 'admin' in user.get('permissions'):
            return func(user, *args, **kwargs)
        else:
            print("Access denied")
    return wrapper


@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")

user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test’']}

delete_user(user1, 101)
delete_user(user2, 102)
delete_user(user3, 103) 
