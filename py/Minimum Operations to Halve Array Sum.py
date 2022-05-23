class Solution:
    def halveArray(self, nums: List[int]) -> int:
        init_sum = sum(nums)
        dest_sum = init_sum / 2
        curr_sum = init_sum
        Q = []
        count = 0
        for num in nums:
            heapq.heappush(Q, -num)
        while count < len(nums) and curr_sum > dest_sum:
            val = -1 * heapq.heappop(Q)
            curr_sum -= val / 2
            heapq.heappush(Q, -(val / 2))
            count += 1
        return count
