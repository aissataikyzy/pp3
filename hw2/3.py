print("Input a dog's age in human years:")
dog_human = float(input())
dog_dog = 0
if(dog_human <= 2):
    dog_dog  = dog_human * 10.5
    print("The dog's age in dog's years is: ", dog_dog)
else:
    a = dog_human - 2
    dog_dog += 21
    b = a * 4
    c = dog_dog + b
    print("The dog's age in dog's years is: ", c)
