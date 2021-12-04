class Solution {
public:
    int nCr(int n, int r) {
	    if (r > n) return 0;
	    if (r * 2 > n) r = n - r;
	    if (r == 0) return 1;
	    if (r == 1) return n;

	    long long res = n;
	    for (int i = 2; i <= r; i++) {
		    res *= (n - i + 1);
		    res /= i;
	    }
	    return (int) res;
    }
    vector<int> getRow(int rowIndex) {
        vector<int> row;
	    for (int i = 0; i <= rowIndex; i++) {
		    row.push_back(nCr(rowIndex, i));
	    }
	    return row;
    }
};
