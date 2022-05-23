class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _sum = 0
        _max = nums[0]
        for item in nums:
            _sum += item
            if _sum > _max:
                _max = _sum
            if _sum < 0:
                _sum = 0
        return _max
