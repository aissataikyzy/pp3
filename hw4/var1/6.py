l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

odd = [l1[i] for i in range(1, len(l1), 2)]

even = [l2[i] for i in range(0, len(l2), 2)]

third_list = odd + even

print("Element at odd-index positions from list one:", odd)
print("Element at even-index positions from list two:", even)
print("Printing Final third list:", third_list)
