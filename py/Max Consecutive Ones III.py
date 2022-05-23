class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        st = 0
        max_val = 0
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if zeros < k:
                    zeros += 1
                else:
                    while nums[st] == 1:
                        st += 1
                    st += 1
            max_val = max(i - st + 1, max_val)
        return max_val
