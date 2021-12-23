class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int> newNums;
        int zeros = 0;
        for (int num : nums) {
            if (num != 0) newNums.push_back(num);
            else zeros++;
        }
        for (; zeros > 0; zeros--) newNums.push_back(0);
        nums = newNums;
    }
};
