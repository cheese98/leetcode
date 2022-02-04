class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
		sort(nums.begin(), nums.end());
		int start = 0, end = nums.size() - 1;
		while (start < end) {
			int sum = nums[start] + nums[end];
			if (sum == target) break;
			else if (sum < target) start++;
			else end--;
		}
		int ans1, ans2;
		for (ans1 = 0; ans1 < nums.size(); ans1++) {
			if (backup[ans1] == nums[start]) break;
		}
		for (ans2 = nums.size() - 1; ans2 >= 0; ans2--) {
			if (backup[ans2] == nums[end]) break;
		}
		return { ans1, ans2 };
	}
};
