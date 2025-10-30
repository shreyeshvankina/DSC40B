import random
def knn_distance(arr, q, k):
	distance = []
	for num in arr:
		distance.append((abs(q - num), num))


	left = 0
	right = len(distance) - 1
	answer = (0,0)

	while left <= right:
		pivot_index = random.randint(left, right)
		pivot = distance[pivot_index]
		distance[pivot_index], distance[right] = distance[right], distance[pivot_index]

		store_index = left
		for i in range(left, right):
			if distance[i][0] < pivot[0]:
				distance[i], distance[store_index] = distance[store_index], distance[i]
				store_index += 1

		distance[store_index], distance[right] = distance[right], distance[store_index]

		if store_index == k-1:
			answer = distance[store_index]
			break
		elif store_index < k-1:
			left = store_index + 1
		else:
			right = store_index - 1

	return answer