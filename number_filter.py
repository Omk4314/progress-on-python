def main():
    numbers = list(range(1,11))
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    prime_numbers = [num for num in numbers if is_prime(num)]
    print(even_numbers)
    print(odd_numbers)
    print(prime_numbers)


def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(pow(n, 0.5)) + 1):
            if n % i == 0:
                return False
    return True

main()

