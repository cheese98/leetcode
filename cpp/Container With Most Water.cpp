class Solution {
public:
	int maxArea(vector<int>& height) {
		int start = 0, end = height.size() - 1, max = 0;
		while (start < end) {
			int water = min(height.at(start), height.at(end)) * (end - start);
			if (max < water) max = water;
			if (height.at(start) <= height.at(end)) start++;
			else end--;
		}
		return max;
	}
};
