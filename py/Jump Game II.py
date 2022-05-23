class Solution:
    def jump(self, nums: List[int]) -> int:
        point = 0; count = 0; dist = 0
        for i in range(len(nums) - 1):
            dist = max(dist, nums[i] + i)
            if i == point:
                count += 1
                point = dist
        return count
