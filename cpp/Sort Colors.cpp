class Solution {
public:
    void sortColors(vector<int>& nums) {
        int colors[3] = {0};
        for (int num : nums) {
            colors[num]++;
        }
        int i = 0, j = 0;
        while(i < nums.size()) {
            if (colors[j] == 0) j++;
            else {
                nums[i++] = j;
                colors[j]--;
            }
        }
    }
};
