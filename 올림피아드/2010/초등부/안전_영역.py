import sys;
input = sys.stdin.readline;
from collections import deque;
dr = [-1,0,1,0];
dc = [0,-1,0,1];

N = int(input());
Board = [] * N;
Visited = None;
for _ in range(N) :
    Board.append(list(map(int, input().split())));

def bfs(i, j, rainLevel) :
    q = deque([(i, j)]);
    Visited[i][j] = 1;
    while q :
        r, c = q.popleft();
        for dir in range(4) :
            nr = r + dr[dir];
            nc = c + dc[dir];
            if nr < 0 or nr >= N or nc < 0 or nc >= N :
                continue;
            if Visited[nr][nc] == 1 :
                continue;
            if Board[nr][nc] > rainLevel :
                q.append((nr, nc));
                Visited[nr][nc] = 1;

def findSafeArea(rainLevel) :
    rtnCnt = 0;
    for i in range(N) :
        for j in range(N) :
            if Board[i][j] <= rainLevel :
                continue;
            if Visited[i][j] == 1 :
                continue;
            rtnCnt += 1;
            bfs(i, j, rainLevel);
    return rtnCnt;

Answer = -1;
for rainlevel in range(0, 101) :
    Visited = [[0] * N for _ in range(N)];
    Answer = max(Answer, findSafeArea(rainlevel));

print(Answer);