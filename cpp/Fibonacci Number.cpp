class Solution {
public:
    int fib(int n) {
        if (n < 2) return n;
        int a[31] = {0, 1};
        for (int i = 2; i <= n; i++) {
            a[i] = a[i - 2] + a[i - 1];
        }
        return a[n];
    }
};
