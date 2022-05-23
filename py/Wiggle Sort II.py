class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n) time
        wig = [0] * 5001
        ans = [0] * len(nums)
        for num in nums:
            wig[num] += 1
        k = 0
        for i in range(0, len(nums), 2):
            while wig[k] == 0:
                k += 1
            ans[i] = k
            wig[k] -= 1
        k = 0
        for i in range(1, len(nums), 2):
            while wig[k] == 0:
                k += 1
            ans[i] = k
            wig[k] -= 1
        k = 0
        while k < len(nums) - 1:
            if ans[k] == ans[k + 1]:
                for i in range(len(nums)):
                    nums[i] = ans[(k + i + 1) % len(nums)]
                break
            k += 1
        if k == len(nums) - 1:
            for i in range(len(nums)):
                nums[i] = ans[i]
