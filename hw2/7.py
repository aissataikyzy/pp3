print("Input a string:" )
string = str(input())
if(string[i] in "0123456789" for i in range(len(string))):
    print("The string is an integer.")
else:
    print("The string is not an integer.")