from collections import deque;

dr = [-1,0,1,0];
dc = [0,1,0,-1];

def solution(board):
    n = len(board);
    d = [[[int(1e9)] * 4 for _ in range(n)] for _ in range(n)]

    d[0][0] = [0, 0, 0, 0];
    q = deque([(0,0,-1,0)]);
    while q :
        r, c, dir, cost = q.popleft();
        for nDir in range(4) :
            added = 0;
            if dir == -1 :
                added = 100;
            elif dir != nDir :
                added = 600;
            else :
                added = 100;
            nr = r + dr[nDir];
            nc = c + dc[nDir];
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 1 :
                nCost = cost + added;
                if nCost < d[nr][nc][nDir] :
                    d[nr][nc][nDir] = nCost;
                    q.append((nr, nc, nDir, nCost));
    return min(d[n - 1][n - 1]);

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]];
print(solution(board));
