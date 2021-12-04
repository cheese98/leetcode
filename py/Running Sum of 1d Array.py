class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for i in range(1, len(nums)):
            for j in range(0, i):
                ans[i] += nums[j]
        return ans
