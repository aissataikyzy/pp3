def find_monotonic_changes(arr):
    changes = []
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            changes.append(i)
    
    return changes

print(find_monotonic_changes([0, 1]))          
print(find_monotonic_changes([0, 2, 1]))       
print(find_monotonic_changes([0, 1, 1, 0]))    
