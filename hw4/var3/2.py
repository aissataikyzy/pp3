def collatz_steps(x):
    steps = 0
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        steps += 1
    return steps

num_test_cases = int(input())

test_cases = list(map(int, input().split()))

for x in test_cases:
    steps = collatz_steps(x)
    print(steps, end=' ')
