# 找到最大或者最小的N个元素
import heapq


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# prints [42, 37, 23]
print(*heapq.nlargest(3, nums))
# prints [-4, 1, 2]
print(*heapq.nsmallest(3, nums))

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
