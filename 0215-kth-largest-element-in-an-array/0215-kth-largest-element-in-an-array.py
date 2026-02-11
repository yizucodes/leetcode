import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # negate all
        max_heap = [-num for num in nums]

        # heapify
        heapq.heapify(max_heap)

        # pop k - 1 times
        for _ in range(k - 1):
            heapq.heappop(max_heap)
            
        return -max_heap[0]