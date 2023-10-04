first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result_set = {(x, y) for x, y in zip(first_list, second_list)}

print(result_set)