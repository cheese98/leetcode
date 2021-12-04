class Solution {
public:
    int climbStairs(int n) {
        int stairs[46] = { 0 };
        stairs[1] = 1;
        stairs[2] = 2;
        for (int i = 3; i <= n; i++) {
            stairs[i] = stairs[i - 2] + stairs[i - 1];
        }
        return stairs[n];
    }
};
