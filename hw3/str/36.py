s = str(input()).split()
count = {}
for c in s:
    if c in count:
        result = c
        break
    else:
        count[c] = 1
if 'result' in locals():
    print(f"First repeating word: {result}")
else:
    print("There are no repeating words in the string")