import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        # num: freq
        freqMap = Counter(nums)

        for num, freq in freqMap.items():
            if len(minHeap) < k:
                # insert in heap (freq, num)
                heapq.heappush(minHeap, (freq, num))
            # elif freq > top of freq of top of Minheap num
            elif freq > minHeap[0][0]:
                # remove top
                heapq.heappop(minHeap)
                # insert new tuple
                heapq.heappush(minHeap, (freq, num))

        # return only values from tuples
        return [num for freq, num in minHeap]