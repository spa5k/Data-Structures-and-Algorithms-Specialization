# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    last = 0
    last_second = 1
    if n <= 1:
        return n

    for i in range(n):
        last, last_second = last_second, last + last_second

    return last


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
