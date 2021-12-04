class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() == 0) return 0;
	    vector<int> ascii;
	    int max = 0;
	    for (int i = 0; i < s.length(); i++) {
	    	int dupl = -1;
	    	for (int j = 0; j < ascii.size(); j++) {
	    		if (ascii[j] == s.at(i)) {
	    			dupl = j;
	    			break;
	    		}
	    	}
	    	ascii.push_back(s.at(i));
	    	for (int j = 0; j <= dupl; j++) {
	    		ascii.erase(ascii.begin());
	    	}
	    	max = max > ascii.size() ? max : ascii.size();
	    }
	    return max;
    }
};
