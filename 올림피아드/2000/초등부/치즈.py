import sys;
input = sys.stdin.readline;
from collections import deque;
dr = [-1,0,1,0];
dc = [0,-1,0,1];

def decideAir() :
    q = deque([]);
    q.append((0, 0));
    Board[0][0] = 2;
    while q :
        r, c = q.popleft();
        for dir in range(4) :
            nr = r + dr[dir];
            nc = c + dc[dir];
            if nr < 0 or nr >= n or nc < 0 or nc >= m :
                continue;
            if Board[nr][nc] != 0 :
                continue;
            q.append((nr, nc));
            Board[nr][nc] = 2;

def decideToBeMelt() :
    for i in range(1, n - 1) :
        for j in range(1, m - 1) :
            if Board[i][j] != 1 :
                continue;
            if Board[i - 1][j] == 2 or Board[i + 1][j] == 2 or Board[i][j - 1] == 2 or Board[i][j + 1] == 2 :
                Board[i][j] = 3;

def melt() :
    for i in range(n) :
        for j in range(m) :
            if Board[i][j] == 3 :
                Board[i][j] = 2;

def checkCheeseCnt() :
    cheeseCnt = 0;
    for i in range(n) :
        for j in range(m) :
            if Board[i][j] == 1 :
                cheeseCnt += 1;
    return cheeseCnt;

def restore() :
    for i in range(n) :
        for j in range(m) :
            if Board[i][j] == 2 :
                Board[i][j] = 0;

n, m = map(int, input().split());
Board = [];
for _ in range(n) :
    Board.append(list(map(int, input().split())));

turnCnt = 1;
remainPecies = checkCheeseCnt();

while True :
    decideAir();
    decideToBeMelt();
    melt();
    cheeseCnt = checkCheeseCnt();
    if cheeseCnt == 0 :
        print(turnCnt);
        print(remainPecies);
        break;
    restore();
    turnCnt += 1;
    remainPecies = cheeseCnt;
