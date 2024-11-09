def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return fib_sequence
    fib_numbers = fibonacci(50)
    sum_fib = sum(fib_numbers)
    print(f"the sum of first 50 fibonacci is: {sum_fib}")