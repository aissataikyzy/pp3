def fib(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        next_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_num)
    return fibonacci

n = int(input())

fibonacci_numbers = fib(n)

cubed_fibonacci = list(map(lambda x: x**3, fibonacci_numbers))

print(cubed_fibonacci)