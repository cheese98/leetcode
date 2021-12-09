class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        unordered_map<int, int> maps;
		for (int x : nums) {
			auto it = maps.find(x);
			if (it == maps.end()) {
				maps.insert(pair<int, int>(x, 1));
			}
			else {
				it->second++;
				if (it->second > nums.size() / 2) {
					return x;
				}
			}
		}
		return 0;
    }
};
