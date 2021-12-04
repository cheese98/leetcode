class Solution {
public:
    int reverse(int x) {
        if (x >= 0){
            int ans = 0;
            while(x > 0){
                if (ans > 214748364){
                    return 0;
                }
                ans = ans * 10 + x % 10;
                x /= 10;
            }
            return ans;
        }
        else{
            int ans = 0;
            if (x == -2147483648) return 0;
            x *= -1;
            while(x > 0){
                if (ans > 214748364){
                    return 0;
                }
                ans = ans * 10 + x % 10;
                x /= 10;
            }
            return -ans;
        }
    }
};
