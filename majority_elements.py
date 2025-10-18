def majority_elements(arr):
    n = len(arr)
    if not arr:
        return []

    # First pass: find potential candidates
    count1 = count2 = 0
    candidate1 = candidate2 = None

    for num in arr:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Second pass: verify counts
    result = []
    for candidate in [candidate1, candidate2]:
        if arr.count(candidate) > n // 3:
            result.append(candidate)

    return sorted(result)
