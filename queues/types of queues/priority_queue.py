import heapq

priority_queue = []

heapq.heappush(priority_queue,(1,'low_priority'))
heapq.heappush(priority_queue,(0,'high_priority'))

result = heapq.heappop(priority_queue)

print(result)
