import sys;
input = sys.stdin.readline;
from collections import deque;

dr = [0,0,0,1,-1];
dc = [0,1,-1,0,0];

def getRightNextDir(nowDir) :
    if nowDir == 1 :
        return 3;
    if nowDir == 2 :
        return 4;
    if nowDir == 3 :
        return 2;
    if nowDir == 4 :
        return 1;

def getLeftNextDir(nowDir) :
    if nowDir == 1 :
        return 4;
    if nowDir == 2 :
        return 3;
    if nowDir == 3 :
        return 1;
    if nowDir == 4 :
        return 2;

n, m = map(int, input().split());
Board = [];
Board.append([0 for _ in range(m + 1)])
for _ in range(n) :
    Board.append([0] + list(map(int, input().split())));

sr, sc, sdir = map(int, input().split());
er, ec, edir = map(int, input().split());

IsVisited = [[[False] * 5 for _ in range(m + 1)] for _ in range(n + 1)];
q = deque([(sr, sc, sdir, 0)]);
IsVisited[sr][sc][sdir] = 0;

answer = -1;
while q :
    nowR, nowC, nowDir, nowDist = q.popleft();
    if nowR == er and nowC == ec and nowDir == edir :
        answer = nowDist;
        break;

    for cnt in range(1, 4) :
        nextR = nowR + cnt * dr[nowDir];
        nextC = nowC + cnt * dc[nowDir];
        if 0 < nextR <= n and 0 < nextC <= m :
            if not IsVisited[nextR][nextC][nowDir] :
                if Board[nextR][nextC] != 1 :
                    q.append((nextR, nextC, nowDir, nowDist + 1));
                    IsVisited[nextR][nextC][nowDir] = True;
                else :
                    break;

    rightNextDir = getRightNextDir(nowDir);
    leftNextDir = getLeftNextDir(nowDir);
    if not IsVisited[nowR][nowC][rightNextDir] :
        q.append((nowR, nowC, rightNextDir, nowDist + 1));
        IsVisited[nowR][nowC][rightNextDir] = True;
    if not IsVisited[nowR][nowC][leftNextDir] :
        q.append((nowR, nowC, leftNextDir, nowDist + 1));
        IsVisited[nowR][nowC][leftNextDir] = True;

print(answer);