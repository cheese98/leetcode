class Solution {
public:
    int rob(vector<int>& nums) {
        int max_one = 0, max_two = 0;
        for (int i = 0; i < nums.size(); i++) {
            int temp = max_two;
            max_two = max(max_two, max_one + nums[i]);
            max_one = temp;
        }
        return max_two;
    }
};
