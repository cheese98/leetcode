class Solution {
public:
    int searchRecursion(vector<int>& nums, int target, int start, int end) {
	    int mid = (start + end) / 2;
	    if (nums.at(mid) == target) return mid;
	    if (start == end) {
	    	if (nums.at(mid) > target) return mid;
	    	else return mid + 1;
	    }
	    if (nums.at(mid) > target) return searchRecursion(nums, target, start, mid);
	    else return searchRecursion(nums, target, mid + 1, end);
    }
    int searchInsert(vector<int>& nums, int target) {
	    return searchRecursion(nums, target, 0, nums.size() - 1);
    }
};
