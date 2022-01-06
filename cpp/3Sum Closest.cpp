class Solution {
public:
	int threeSumClosest(vector<int>& nums, int target) {
		int closest = 99999;
		sort(nums.begin(), nums.end());
		for (int i = 0; i < nums.size() - 2; i++) {
			int j = i + 1, k = nums.size() - 1;
			while (j < k) {
				int sum = nums[i] + nums[j] + nums[k];
				if (sum == target) return sum;
				if (abs(target - sum) < abs(target - closest)) {
					closest = sum;
				}
				if (sum <target) j++;
				else k--;
			}
		}
		return closest;
	}
};
