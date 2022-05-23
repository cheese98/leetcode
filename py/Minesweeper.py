class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        dx = [0, -1, -1, -1, 0, 1, 1, 1]
        dy = [1, 1, 0, -1, -1, -1, 0, 1]
        visited = [[0 for j in range(len(board[0]))]
                   for i in range(len(board))]
        queue = deque()
        queue.append(click)
        visited[click[0]][click[1]] = 1
        while queue:
            xx, yy = queue.popleft()
            if board[xx][yy] != 'M':
                adjs = []
                for i in range(8):
                    adj_x = xx + dx[i]
                    adj_y = yy + dy[i]
                    if adj_x >= 0 and adj_x < len(board) \
                            and adj_y >= 0 and adj_y < len(board[0]):
                        adjs.append((adj_x, adj_y))
                bomb_count = 0
                for adj in adjs:
                    if board[adj[0]][adj[1]] == 'M':
                        bomb_count += 1
                if bomb_count > 0:
                    board[xx][yy] = str(bomb_count)
                else:
                    board[xx][yy] = 'B'
                    for adj in adjs:
                        if visited[adj[0]][adj[1]] == 0:
                            queue.append(adj)
                            visited[adj[0]][adj[1]] = 1
        return board
