import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

while True: 
    a = input("Введіть номер числа Фібоначчі (або 'break' для виходу): ")
    try:
        if a.lower().strip() in ['break', "'break'", '"break"']:
            break
        else:
            start_time1 = time.perf_counter()
        
            a = int(a)
            result = fibonacci(a)
            print()
            print(f"F({a}) = {result}")
        
            end_time1 = time.perf_counter()
            print(f"Час першого виконання : {end_time1 - start_time1} секунд")
        
            start_time2 = time.perf_counter()
            result = fibonacci(a)
            print()
            print(f"F({a}) = {result}")
            end_time2 = time.perf_counter()
        
            print(f"Час виконання 2: {end_time2 - start_time2} секунд")
            print()
            print(f'Різниця склала: {(end_time1 - start_time1) - (end_time2 - start_time2)}')
            print('=========================================================')
    except ValueError:
        print("Некоректний формат вводу !!\nМожливе введення тільки цілих чисел (або 'break' для виходу)!")
        print('=========================================================')
    except RecursionError:
        print('Число фібоначі завелике\nВиберіть інше число')
        print('=========================================================')
    except Exception as e:
        print(e)
        print('=========================================================')
print('Приємно було працювати\nДо побачення!')
