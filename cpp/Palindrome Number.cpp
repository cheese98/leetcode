class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int lst[11] = {0};
        int len = 0;
        while(x > 0){
            lst[len++] = x % 10;
            x /= 10;
        }
        for(int i=0;i<len-1-i;i++){
            if(lst[i] != lst[len-1-i]){
                return false;
            }
        }
        return true;
    }
};
