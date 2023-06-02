import sys;
input = sys.stdin.readline;

R, C = map(int, input().split());
Board = [];
for _ in range(R) :
    Board.append(list(map(int, input().split())));

dr = [-1,0,1,0];
dc = [0,-1,0,1];
d = [[[-1] * 4 for _ in range(C)] for _ in range(R)];

def oob(r, c) :
    if r < 0 or r >= R or c < 0 or c >= C :
        return True;
    return False;

def dfs(r, c, dir) :
    if r == R - 1 and c == C - 1 :
        d[r][c][dir] = 1;
        return d[r][c][dir];

    if d[r][c][dir] != -1 :
        return d[r][c][dir];

    temp = 0;
    for nDir in range(4) :
        nr = r + dr[nDir];
        nc = c + dc[nDir];
        if oob(nr, nc) :
            continue;
        if Board[nr][nc] >= Board[r][c] :
            continue;
        temp += dfs(nr, nc, nDir);

    d[r][c][dir] = temp;
    return d[r][c][dir];

dfs(0, 0, 0);
print(d[0][0][0]);