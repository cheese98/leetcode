class Solution {
public:
    int tribonacci(int n) {
        int n0 = 0, n1 = 1, n2 = 1, n3;
        if (n < 2) return n;
        if (n == 2) return 1;
        for (int i = 3; i <= n; i++) {
            n3 = n2 + n1 + n0;
            n0 = n1;
            n1 = n2;
            n2 = n3;
        }
        return n3;
    }
};
