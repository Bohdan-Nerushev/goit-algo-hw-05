import time

def caching_fibonacci():
    cache = {}  # dictionary to store computed values

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:  # checking if the result is already in the cache
            return cache[n]
        
        # Calculating Fibonacci number and storing the result in the cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

start_time1 = time.perf_counter()
print(fib(10))
end_time1 = time.perf_counter()
print(f"First execution time: {end_time1 - start_time1} seconds")

start_time2 = time.perf_counter()
print(fib(10))      
end_time2 = time.perf_counter()
print(f"Second execution time: {end_time2 - start_time2} seconds")

print()

print(f'Difference: {(end_time1 - start_time1) - (end_time2 - start_time2)}')
