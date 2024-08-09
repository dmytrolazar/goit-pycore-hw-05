def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        nonlocal cache
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci

def main():
    fib = caching_fibonacci()
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610

if __name__ == '__main__':
    main()