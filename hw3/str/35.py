s = str(input())
count = {}
for c in s:
    if c in count:
        result = c
        break
    else:
        count[c] = 1
if 'result' in locals():
    print(f"First repeating character: {result}")
else:
    print("There are no repeating characters in the string")