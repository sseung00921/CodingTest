import sys;
input = sys.stdin.readline;

n, m = map(int, input().split());
Board = [];
for _ in range(n) :
    Board.append(list(map(int, input().split())));

d = [[-1] * m for _ in range(n)];
dr = [-1,0,1,0];
dc = [0,-1,0,1];

def dfs(r, c) :
    if r == n - 1 and c == m - 1 :
        return 1;

    if d[r][c] != -1 :
        return d[r][c];

    summ = 0;
    for dir in range(4) :
        nr = r + dr[dir];
        nc = c + dc[dir];
        if nr < 0 or nr >= n or nc < 0 or nc >= m :
            continue;
        if Board[nr][nc] < Board[r][c] :
            summ += dfs(nr, nc);

    d[r][c] = summ;
    return d[r][c];

print(dfs(0,0));