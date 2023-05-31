import sys;
input = sys.stdin.readline;
from collections import deque;

dr = [1,0,-1,0];
dc = [0,1,0,-1];

R, C = map(int, input().split());
Board = [];
for _ in range(R) :
    Board.append(input().rstrip());

Answer = -1;

def bfs(sR, sC) :
    global Answer;
    distBoard = [[-1] * C for _ in range(R)];
    q = deque([(sR, sC, 0)]);
    distBoard[sR][sC] = 0;

    while q :
        nowR, nowC, nowDist = q.popleft();

        if nowDist != 0 :
            Answer = max(Answer, nowDist);

        for dir in range(4) :
            nextR = nowR + dr[dir];
            nextC = nowC + dc[dir];
            if nextR < 0 or nextR >= R or nextC < 0  or nextC >= C :
                continue;
            if Board[nextR][nextC] == 'W' :
                continue;
            if distBoard[nextR][nextC] != -1 :
                continue;
            q.append((nextR, nextC, nowDist + 1));
            distBoard[nextR][nextC] = nowDist + 1;

    return;

for i in range(R) :
    for j in range(C) :
        if Board[i][j] == 'W' :
            continue;
        bfs(i, j);

print(Answer);
