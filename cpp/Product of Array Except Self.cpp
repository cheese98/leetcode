class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prod = 1, zeros = 0;
        vector<int> r;
        for (int num : nums) {
            if (num != 0) prod *= num;
            else zeros++;
        }
        if (zeros > 1) {
            for(int i = 0; i < nums.size(); i++) r.push_back(0);
        }
        else if (zeros == 1) {
            for(int i = 0; i < nums.size(); i++) {
                if (nums[i] == 0) r.push_back(prod);
                else r.push_back(0);
            }
        }
        else {
            for (int num : nums) r.push_back(prod / num);
        }
        return r;
    }
};
