class Solution {
public:
    int lengthOfLastWord(string s) {
	    int i = s.length() - 1;
	    for (; i >= 0 && s.at(i) == ' '; i--);
	    int j = i;
	    for (; i >= 0 && s.at(i) != ' '; i--);
	    return j - i;
    }
};
