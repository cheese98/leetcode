class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() == 0) return 0;
        int st = 0;
	    int max = 1;
	    for (int i = 1; i < s.length(); i++) {
	    	int dupl = -1;
	    	for (int j = st; j < i; j++) {
	    		if (s[j] == s[i]) {
	    			dupl = j;
	    			break;
	    		}
	    	}
            if (dupl != -1) st = dupl + 1;
	    	max = max > i + 1 - st ? max : i + 1 - st;
	    }
	    return max;
    }
};