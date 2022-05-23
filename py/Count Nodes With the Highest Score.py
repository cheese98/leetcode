class Solution:
    def recursive(self, num_childs, childs, idx):
        num_childs[idx] = 1
        for cc in childs[idx]:
            self.recursive(num_childs, childs, cc)
            num_childs[idx] += num_childs[cc]
        
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        childs = [[] for _ in range(len(parents))]
        num_childs = [0 for _ in range(len(parents))]
        
        for i in range(1, len(parents)):
            childs[parents[i]].append(i)
        self.recursive(num_childs, childs, 0)
        
        temp = 1
        ress = []
        for cc in childs[0]:
            temp *= num_childs[cc]
        ress.append(temp)
        for i in range(1, len(parents)):
            if len(childs[i]) == 0:
                ress.append(len(parents) - 1)
            else:
                temp = 1
                for cc in childs[i]:
                    temp *= num_childs[cc]
                temp *= len(parents) - num_childs[i]
                ress.append(temp)
        ress.sort()
        counter = len(parents) - 1
        while counter > 0 and ress[counter] == ress[counter - 1]:
            counter -= 1
        return len(parents) - counter
