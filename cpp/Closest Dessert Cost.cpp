class Solution {
public:
    map<int, int> price;

	void recursive(vector<int> topping, int sum, int index) {
		price[sum]++;
		price[sum + topping[index]]++;
		price[sum + 2 * topping[index]]++;
		if (index < topping.size() - 1) {
			recursive(topping, sum, index + 1);
			recursive(topping, sum + topping[index], index + 1);
			recursive(topping, sum + 2 * topping[index], index + 1);
		}
	}
	int closestCost(vector<int>& baseCosts, vector<int>& toppingCosts, int target) {
		int closest = 1000000000;
		recursive(toppingCosts, 0, 0);
		vector<int> toppings;
		for (auto it = price.begin(); it != price.end(); it++) {
			toppings.push_back(it->first);
		}
		for (int topping : toppings) {
			for (int base : baseCosts) {
				int sum = base + topping;
				int oldDiff = abs(closest - target);
				int newDiff = abs(sum - target);
				if (newDiff < oldDiff || newDiff == oldDiff && sum < closest) {
					closest = sum;
					if (target == closest) return closest;
				}
			}
		}
		return closest;
	}
};
