import math

def gcd(x,y):
    if x==y:
        return x
    elif x>y:
        return gcd(x-y,y)
    else:
        return gcd(x,y-x)

print("Select operation.")
print("1.GCD/LCM")
print("2.Factors")
print("3.Prime factor")
# print("4.Divide")

choice = input("Enter choice: 1, 2, or 3: ")

if choice == '1':
    a, b = input("Enter numbers: ").split(",")
    a, b = int(a), int(b)
    print("GCD: " + str(gcd(a, b)))
    print("LCM: " + str(a * b // gcd(a, b)))


elif choice == '2':
    number = int(input("Enter a number for factors: "))
    factors = []

    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factor_pair = number // i
            if factor_pair != i:
                factors.append(factor_pair)

    factors.sort()
    print(factors)


elif choice == '3':
    number=int(input("Enter number for prime factor: "))
    factors=[]
    while number %2==0:
        factors.append(2)
        number //=2
    divisor=3
    while number !=1 and divisor <= number:
        if number %divisor==0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor +=2
    print("The prime factors are: ")
    for i in range (len(factors)):
        print(factors[i],end=', ')

else:
   print("Invalid input")

