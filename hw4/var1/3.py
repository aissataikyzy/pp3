def match(a, l):
    b = []

    c = {i: char for i, char in enumerate(a) if char != '*'}

    for string in l:
        if len(string) != len(a):
            continue  

        is_match = True
        for position, char in c.items():
            if string[position] != char:
                is_match = False
                break

        if is_match:
            b.append(string)

    return b

a = "a**a****"
l = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
matching_strings = match(a, l)

if matching_strings:
    print("Matching strings are:", matching_strings)
else:
    print("No matching strings found.")