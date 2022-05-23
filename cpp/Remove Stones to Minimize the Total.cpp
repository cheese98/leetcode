class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
		priority_queue<int> queue;
		for (int pile : piles) {
			queue.push(pile);
		}
		for (int i = 0; i < k; i++) {
			int elem = queue.top();
			queue.pop();
			queue.push((elem + 1) / 2);
		}
		int sum = 0;
		while (!queue.empty()) {
			sum += queue.top();
			queue.pop();
		}
		return sum;
	}
};
