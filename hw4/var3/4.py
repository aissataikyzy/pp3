def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  

    primes = []
    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return primes

num_primes = int(input())

positions = list(map(int, input().split()))

limit = 300000
prime_list = sieve_of_eratosthenes(limit)

for position in positions:
    prime_at_position = prime_list[position - 1]  
    print(prime_at_position, end=' ')
