def swap_sum(A, B):
    sumA = sum(A)
    sumB = sum(B)
    
    target = (sumB - sumA - 10) // 2
    i = 0
    j = 0
    lenA = len(A)
    lenB = len(B)
    while i < lenA and j < lenB:
        diff = B[j] - A[i]
        if diff == target:
            return (i, j)
        elif diff < target:
            j += 1
        else:
            i += 1
    return None