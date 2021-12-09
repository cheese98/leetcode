class Solution {
public:
    int tribonacci(int n) {
        int a[38] = {0, 1, 1};
        for (int i = 3; i <= n; i++) {
            a[i] = a[i - 3] + a[i - 2] + a[i - 1];
        }
        return a[n];
    }
};