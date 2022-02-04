class RecentCounter:

    def __init__(self):
        self.reqs = []

    def ping(self, t: int) -> int:
        self.reqs.append(t)
        while len(self.reqs) > 0 and self.reqs[0] + 3000 < t:
            self.reqs.pop(0)
        return len(self.reqs)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
