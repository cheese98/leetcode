class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;
	    vector<int> row1;
    	    row1.push_back(1);
	    triangle.push_back(row1);
	    for (int i = 2; i <= numRows; i++) {
	    	vector<int> row;
	    	row.push_back(1);
	    	for (int j = 1; j < i - 1; j++) {
	    		row.push_back(triangle[i - 2][j - 1] + triangle[i - 2][j]);
	    	}
	    	row.push_back(1);
	    	triangle.push_back(row);
	    }
	    return triangle;
    }
};
