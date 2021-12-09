class Solution {
public:
    int strStr(string haystack, string needle) {
	    return needle.size() == 0 ? 0 : haystack.find(needle);
    }
};
