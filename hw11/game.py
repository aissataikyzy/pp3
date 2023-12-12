def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def worst_case_cost(n, a, b, fib):
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = min(a + dp[i-1], b + dp[i-2])

    return dp[n]

def main():
    n = 10**12
    a = 5
    b = 7

    fib = fibonacci(n)
    result = sum(worst_case_cost(n, a, b, fib[i]) for i in range(1, 131))

    print(f"{result:.8f}")

if __name__ == "__main__":
    main()
