def less_than_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

n = int(input())
print(less_than_thousand(n))