class Solution {
public:
    int fib(int n) {
        if (n < 2) return n;
        int n0 = 0, n1 = 1, n2 = 1;
        for (int i = 1; i < n; i++) {
            n2 = n0 + n1;
            n0 = n1;
            n1 = n2;
        }
        return n2;
    }
};
