year = int(input("Input your birth year: "))
if((year - 2000) % 12 == 0):
    print("Dragon")
elif((year - 2000) % 12 == 1):
    print("Snake")
elif((year - 2000) % 12 == 2):
    print("Horse")
elif((year - 2000) % 12 == 3):
    print("Goat")
elif((year - 2000) % 12 == 4):
    print("Monkey")
elif((year - 2000) % 12 == 5):
    print("Rooster")
elif((year - 2000) % 12 == 6):
    print("Dog")
elif((year - 2000) % 12 == 7):
    print("Pig")
elif((year - 2000) % 12 == 8):
    print("Rat")
elif((year - 2000) % 12 == 9):
    print("Ox")
elif((year - 2000) % 12 == 10):
    print("Tiger")
else:
    print("Rabbit")
