import sys;
from collections import deque;

input = sys.stdin.readline;
dr = [-1,0,1,0];
dc = [0,-1,0,1];

def dfs(sr, sc, givenNum) :
    visited = [[0] * n for _ in range(n)];
    visited[sr][sc] = 1;
    q = deque([(sr, sc)]);
    board[sr][sc] = givenNum;

    while q :
        r, c = q.popleft();
        for dir in range(4) :
            nr = r + dr[dir];
            nc = c + dc[dir];
            if nr < 0 or nr >= n or nc < 0 or nc >= n :
                continue;
            if board[nr][nc] == '0' :
                continue;
            if visited[nr][nc] == 1 :
                continue;
            visited[nr][nc] = 1;
            q.append((nr, nc));
            board[nr][nc] = givenNum;

n = int(input());
board = [];
for _ in range(n) :
    board.append(list(input().rstrip()));

givenNum = 2;
for i in range(n) :
    for j in range(n) :
        if board[i][j] == '1' :
            dfs(i, j, givenNum);
            givenNum += 1;

checkArr = [0] * 625;
for i in range(n) :
    for j in range(n) :
        if board[i][j] != '0' and board[i][j] != '1' :
            checkArr[board[i][j]] += 1;

totalDanjiCnt = 0;
cntInEachDanjiArr = [];
for i in range(len(checkArr)) :
    if checkArr[i] != 0 :
        totalDanjiCnt += 1;
        cntInEachDanjiArr.append(checkArr[i]);

print(totalDanjiCnt);
cntInEachDanjiArr.sort();
for cnt in cntInEachDanjiArr :
    print(cnt);