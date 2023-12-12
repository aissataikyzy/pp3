N = int(input())

# Part 1
s = 0
for i in range(int(N**0.5)+1):
    for j in range(int(N**0.5)+1):
        if i**2 + j**2 == N and i < j:
            print(i, j, end=', ')
            s += i
print()
print(s)

# Part 2
l = [S for S in range(1, N) if all(i**2 + j**2 != S for i in range(1, int(S**0.5)+1) for j in range(1, int(S**0.5)+1))]

# Part 3
k4_1 = [i*4+1 for i in range(1, int(150/4)) if all((i*4+1) % j != 0 for j in range(2, i*2+1))]

# Part 4
S = sum(i for i in l if any(i % j == 0 for j in k4_1))
print()
print(S)
