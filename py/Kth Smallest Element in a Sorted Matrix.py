import numpy as np
class Solution:
    # Source: http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf
    def pick(self, L, p):
        return L[p - 1]

    def rank_minus(self, A, a):
        x = 0
        for i in range(len(A)):
            j = 0
            while j < len(A) and A[i][j] < a:
                j += 1
            x += j
        return x

    def rank_plus(self, A, a):
        x = 0
        for i in range(len(A)):
            j = len(A) - 1
            while j >= 0 and A[i][j] > a:
                j -= 1
            x += len(A) - 1 - j
        return x

    def biselect(self, n, A, k1, k2):
        if n == 1:
            return (A[0][0], A[0][0])
        if n == 2:
            B = [A[0][0], A[0][1], A[1][0], A[1][1]]
            B.sort()
            return (B[k1 - 1], B[k2 - 1])
        N = math.ceil(1/2 * (n + 1))
        AA = []
        iter_list = [i for i in range(0, n, 2)]
        if n % 2 == 0:
            iter_list.append(n - 1)
        for i in iter_list:
            row = []
            for j in iter_list:
                row.append(A[i][j])
            AA.append(row)
        K1 = math.ceil(k1 / 4) + n + \
            1 if n % 2 == 0 else math.ceil(1/4 * (k1 + 2 * n + 1))
        K2 = math.floor(1/4 * (k2 + 3))
        (a, b) = self.biselect(N, AA, K1, K2)
        RA = self.rank_minus(A, a)
        RB = self.rank_plus(A, b)
        L = []
        for i in range(len(A)):
            for j in range(len(A[i])):
                if b < A[i][j] and A[i][j] < a:
                    L.append(A[i][j])
        L.sort()
        if RA <= k1 - 1:
            x = a
        elif k1 + RB - n * n <= 0:
            x = b
        else:
            x = self.pick(L, k1 + RB - n * n)
        if RA <= k2 - 1:
            y = a
        elif k2 + RB - n * n <= 0:
            y = b
        else:
            y = self.pick(L, k2 + RB - n * n)
        return (x, y)
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        (x, y) = self.biselect(len(matrix), matrix, k, k)
        return x
