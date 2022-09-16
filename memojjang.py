import sys;
input = sys.stdin.readline;

n, m = map(int, input().split());
Board = [[0] * m for _ in range(n)];
d = [[-1] * m for _ in range(n)];

dr = [-1,0,1,0];
dc = [0,1,0,-1];
for i in range(n) :
    data = list(map(int, input().split()));
    for j in range(len(data)) :
        Board[i][j] = data[j];

def dfs(r, c) :
    if r == n - 1 and c == m - 1 :
        return 1;

    if d[r][c] != -1 :
        return d[r][c];

    ways = 0;
    for dir in range(4) :
        nr = r + dr[dir];
        nc = c + dc[dir];
        if nr < 0 or nr >= n or nc < 0 or nc >= m :
            continue;
        if Board[nr][nc] < Board[r][c] :
            ways += dfs(nr, nc);

    d[r][c] = ways;
    return d[r][c];


print(dfs(0,0));
