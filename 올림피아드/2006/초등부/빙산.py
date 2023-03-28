import sys;
input = sys.stdin.readline;
from collections import deque;

dr = [-1,0,1,0];
dc = [0,-1,0,1];
R, C = map(int, input().split());
board = [];
for _ in range(R) :
    board.append(list(map(int, input().split())));

Visited = None
def tripOnOneIceMoutain(r, c) :
    Visited[r][c] = True;
    q = deque([(r, c)])
    while q :
        r, c = q.popleft();
        for dir in range(4) :
            nr = r + dr[dir];
            nc = c + dc[dir];
            if nr < 0 or nr >= R or nc < 0 or nc >= C :
                continue;
            if Visited[nr][nc] == True :
                continue;
            if board[nr][nc] > 0 :
                Visited[nr][nc] = True;
                q.append((nr, nc));
    return;

def meltDuringOneYear() :
    tBoard = [[0] * C for _ in range(R)];
    for i in range(R) :
        for j in range(C) :
            if board[i][j] > 0 :
                valueBeforeMelt = board[i][j];
                for dir in range(4) :
                    ni = i + dr[dir];
                    nj = j + dc[dir];
                    if ni < 0 or ni >= R or nj < 0 or nj >= C :
                        continue;
                    if board[ni][nj] == 0 :
                        valueBeforeMelt -= 1;
                valueAfterMelt = max(0, valueBeforeMelt);
                tBoard[i][j] = valueAfterMelt;
    return tBoard;

elapsedYear = 1;
while True :
    board = meltDuringOneYear();
    Visited = [[False] * C for _ in range(R)];

    isCompleteTripOnOneMoutain = False;
    for i in range(R) :
        for j in range(C) :
            if board[i][j] > 0 :
                tripOnOneIceMoutain(i, j);
                isCompleteTripOnOneMoutain = True;
                break;
        if isCompleteTripOnOneMoutain :
            break;

    isOneMoutain = True;
    nonZeroCnt = 0;
    for i in range(R) :
        for j in range(C) :
            if board[i][j] > 0 :
                nonZeroCnt += 1;
            if Visited[i][j] == False and board[i][j] > 0 :
                isOneMoutain = False;
                break;
        if not isOneMoutain :
            break;

    if not isOneMoutain :
        print(elapsedYear);
        break;

    if nonZeroCnt == 0 :
        print(0);
        break;

    elapsedYear += 1;