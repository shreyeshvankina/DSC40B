def histogram(points, bins):
    n = len(points)
    densities = []
    
    # pointer to the current point
    current_index = 0
    
    for start, end in bins:
        count_in_bin = 0
        while current_index < n and points[current_index] < end:
            count_in_bin += 1
            current_index += 1
        bin_width = end - start
        density = count_in_bin / (n * bin_width)
        densities.append(density)
    
    return densities



points = [1, 2, 3, 6, 7, 9, 10, 11]
bins = [(0, 4), (4, 8), (8, 12)]
print(histogram(points, bins))