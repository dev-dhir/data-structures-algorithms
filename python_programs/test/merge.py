i, j = 0, 0
merged = []
while len(merged) < len(arr1) + len(arr2):
    if arr1[i] <= arr2[j]:
        merged.append(arr1[i])
        if i < len(arr1) - 1:
            i += 1
        else:
            merged.extend(arr2[j:])
            break
    else:
        merged.append(arr2[j])
        if j < len(arr2) - 1:
            j += 1
        else:
            merged.extend(arr1[i:])
            break
        

print(merged)
