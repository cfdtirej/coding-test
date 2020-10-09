def decimal_to_radix(n, base):
    result = ''
    while n > 0:
        result = str(n % base) + result
        n //= base
    return result


if __name__ == '__main__':
    n = 23
    print(decimal_to_radix(n, 2))
    print(decimal_to_radix(n, 3))
