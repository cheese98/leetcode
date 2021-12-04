class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size() == 1) return nums[0];
        int sum = 0, _max = nums[0];
        for(int item : nums){
            sum += item;
            _max = max(sum, _max);
            sum = max(sum, 0);
        }
        return _max;
    }
};
