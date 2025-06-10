"""
find the largest k element
"""
import heapq


array = [10,40,80,4,7,90,45,79,50]

min_heap = []

k = 3

for element in array:
    if len(min_heap) < k:
        heapq.heappush(min_heap, element)
    else:
         if element > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, element)


sorted_result = sorted(min_heap, reverse=True)
print(sorted_result)
