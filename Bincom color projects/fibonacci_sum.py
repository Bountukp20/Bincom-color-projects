def fibonacci_sum(n):
    fib_sum = 0
    fib_prev = 0
    fib_current = 1

    for _ in range(n):
        fib_sum += fib_current
        fib_next = fib_prev + fib_current
        fib_prev = fib_current
        fib_current = fib_next

    return fib_sum

# Calculate the sum of the first 50 Fibonacci numbers
sum_first_50_fib = fibonacci_sum(50)
print(f"Sum of the first 50 Fibonacci numbers: {sum_first_50_fib}")
