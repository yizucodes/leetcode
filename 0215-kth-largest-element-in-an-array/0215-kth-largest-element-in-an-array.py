import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # init min_heap
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                # insert
                heapq.heappush(min_heap, num)
            else:
                # check if num > top of heap
                if num > min_heap[0]:
                    # if it is replace with num
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)

        return min_heap[0]