def print_indices_and_elements(elements) -> None:
    for i, e in enumerate(elements):
        print(f'{i} {e}')
    pass


def get_even_numbers_between(start: int, end: int) -> list[int]:
    return [i for i in range(start, end+1) if i % 2 == 0]


def get_char_set_from(s: str) -> set[str]:
    return {c for c in s if c.isalpha()}


def get_perfect_squares_between(start: int, end: int) -> dict[int,int]:
    return {i: i**(1/2) for i in range(start, end+1) if i**(1/2) == int(i**(1/2))}


def filter_even_from(numbers: list[int]) -> list[int]:
    return [i for i in numbers if i % 2 == 0]


def get_number_or_minus_one(n: int) -> int:
    return n if n%2==0 else -1


def transform_multiples_of_5(numbers: list[int]) -> list[int]:
    return [-1 if i % 2 != 0 and i % 5 == 0 else i for i in numbers if i % 5 == 0]


def str_lengths(strings: list[str]) -> list[int]:
    return [len(s) for s in strings]


def get_fibonacci_type(version: int) -> str:
    return "generator" if version == 1 else "list"


def difference_between_fibonacci1_and_fibonacci2() -> str:
    return '''The Generator function has a lower memory usage than the "normal" function, this is due to the fact that generators are still stored in memory after yielding and thus dont need to
              store the values in a list, like this example. Although the memory usage is less, the fact that you need to return to the memory to grab the previous state of the function means that
              the Generator is on average slower to run than the regular for loop with a return statement in the end.'''


class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
        self.index = 0
        # You can add more code here if you need
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.elements):
            raise StopIteration
        else:
            value = self.elements[self.index]
            self.index += 2
            return value
        


def my_avg(e1: float, e2: float, *others: tuple[float]) -> float:
    return (e1 + e2 + sum(others)) / (2 + len(others))


def keys_with_different_value() -> list[int]:
    a = dict(zip(range(10), range(10)))
    b = dict(zip(range(5, 15), range(15, 25)))
    c = {**a, **b}
    d = {**b, **a}
    return sorted([k for k, vc in c.items() if vc != d[k]])


def print_out_in(*numbers) -> None:
    numbers = list(numbers)
    while len(numbers) > 1:
        first, *middle, last = numbers
        print(first, last)
        numbers = middle
    if numbers:
        print(numbers[0])


def append_range(start, end, step=1, to=None):
    if to is None:
        to = []
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    global global_var 
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value is None
