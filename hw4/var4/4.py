def arithmetic_sequence_sum(A, B, N):
    return N * (2 * A + (N - 1) * B) // 2

num_test_cases = int(input())

for _ in range(num_test_cases):
    A, B, N = map(int, input().split())
    result = arithmetic_sequence_sum(A, B, N)
    print(result, end=' ')

print()