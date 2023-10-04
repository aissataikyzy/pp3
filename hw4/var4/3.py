def max_candies(isles):
    n = len(isles)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):

        dp[i] = max(dp[i - 1], isles[i - 1])
        
        if i > 1:
            dp[i] = max(dp[i], dp[i - 2] + isles[i - 1])
    
    return dp[n]


num_test_cases = int(input())

for _ in range(num_test_cases):
    isles = list(map(int, input().split()))
    result = max_candies(isles)
    print(result)