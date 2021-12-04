class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int i, max = 0;
        vector<bool> ans;
        for(i=0;i<candies.size();i++){
            if(max < candies[i]) max = candies[i];
        }
        for(i=0;i<candies.size();i++){
            ans.push_back(bool(candies[i] + extraCandies >= max));
        }
        return ans;
    }
};
