# task3.py
import time

def decorator_1(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)
        end_time = time.time()  # Record the end time
        print(f"{func.__name__} call executed in {end_time - start_time:.4f} sec")
        return result
    return wrapper
