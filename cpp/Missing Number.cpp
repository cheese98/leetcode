class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
	    unordered_map <int, char> map;
	    for (int val : nums) {
		    map.insert({ val, 0 });
	    }
	    int i;
	    for (i = 0; i <= n; i++) {
		    if (map.find(i) == map.end()) {
			    break;
		    }
	    }
	    return i;
    }
};
