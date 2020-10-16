def fibonacci_1(n):
    if (n == 1) or (n == 2):
        return 1
    return fibonacci_1(n - 2) + fibonacci_1(n - 1)

memo = {1: 1, 2: 1}
def fibonacci_2(n):
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_2(n - 2) + fibonacci_2(n - 1)
    return memo[n]

def fibonacci_3(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])
    return fib[n - 1]


if __name__ == '__main__':
    print(fibonacci_1(6))
    print(fibonacci_2(6))
    print(fibonacci_3(6))