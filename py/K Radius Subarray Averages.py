class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        R = 2 * k + 1
        res = [-1 for i in range(len(nums))]
        if len(nums) < k:
            return res
        curr = sum(nums[:R])
        for i in range(k, len(nums) - k):
            res[i] = curr // R
            if i + k + 1 == len(nums):
                break
            curr += nums[i + k + 1] - nums[i - k]
        return res
