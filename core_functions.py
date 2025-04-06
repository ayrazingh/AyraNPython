import re

def is_valid_name(name):
    if re.match("^[A-Za-z\s]+$", name):
        return True
    else:
        return False


def fibonacci(num):
    fib_sequence = [0, 1]
    for i in range(2, num):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    if n <= 1:  # Prime numbers are greater than 1
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:  # If divisible by any number between 2 and sqrt(n)
            return False
    return True


def check_even_or_odd(n):
    if n % 2 == 0:
        return f"{n} is an Even number."
    else:
        return f"{n} is an Odd number."


def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

