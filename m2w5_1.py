from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


class Calculator:
    @timeit
    def calc(self, num):
        """
        an example function that returns sum of all numbers up to the square of num
        """
        total = sum((x for x in range(0, num**2)))
        return total

    def __repr__(self):
        return f'calc_object:{id(self)}'


if __name__ == '__main__':
    calc = Calculator()
    calc.calc(10)
    calc.calc(100)
    calc.calc(1000)
    calc.calc(5000)
    calc.calc(10000)