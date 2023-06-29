import sys;
input = sys.stdin.readline;
from collections import deque;

M, N, H = map(int, input().split());

def ib(kind, val) :
    if kind == "M" :
        return 0 <= val < M;
    elif kind == "N" :
        return 0 <= val < N;
    elif kind == "H" :
        return 0 <= val < H;

def calPosByH(h) :
    return h*N;

Board = []
for h in range(H) :
    for _ in range(N) :
        Board.append(list(map(int, input().split())));

q = deque([]);
for rh in range(N*H) :
    for c in range(M) :
        if Board[rh][c] == 1 :
            h = rh // N;
            r = rh % N;
            q.append((r, c, h))

while q :
    nowR, nowC, nowH = q.popleft();
    if ib("N", nowR + 1) :
        nextR = nowR + 1;
        if Board[nextR + N*nowH][nowC] == 0 :
            Board[nextR + N*nowH][nowC] = Board[nowR + N*nowH][nowC] + 1;
            q.append((nextR, nowC, nowH));
    if ib("N", nowR - 1) :
        nextR = nowR - 1;
        if Board[nextR + N*nowH][nowC] == 0 :
            Board[nextR + N*nowH][nowC] = Board[nowR + N*nowH][nowC] + 1;
            q.append((nextR, nowC, nowH));
    if ib("M", nowC + 1) :
        nextC = nowC + 1;
        if Board[nowR + N*nowH][nextC] == 0 :
            Board[nowR + N*nowH][nextC] = Board[nowR + N*nowH][nowC] + 1;
            q.append((nowR, nextC, nowH));
    if ib("M", nowC - 1) :
        nextC = nowC - 1;
        if Board[nowR + N*nowH][nextC] == 0 :
            Board[nowR + N*nowH][nextC] = Board[nowR + N*nowH][nowC] + 1;
            q.append((nowR, nextC, nowH));
    if ib("H", nowH + 1) :
        nextH = nowH + 1;
        if Board[nowR + N*nextH][nowC] == 0 :
            Board[nowR + N*nextH][nowC] = Board[nowR + N*nowH][nowC] + 1;
            q.append((nowR, nowC, nextH));
    if ib("H", nowH - 1) :
        nextH = nowH - 1;
        if Board[nowR + N*nextH][nowC] == 0 :
            Board[nowR + N*nextH][nowC] = Board[nowR + N*nowH][nowC] + 1;
            q.append((nowR, nowC, nextH));

Answer = -1;
IsExistNotRipen = False;
for r in range(N*H) :
    for c in range(M) :
        Answer = max(Answer, Board[r][c]);
        if Board[r][c] == 0 :
            IsExistNotRipen = True;

if IsExistNotRipen :
    print(-1);
else :
    print(Answer - 1);