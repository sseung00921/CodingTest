import sys;
input = sys.stdin.readline;

n, m = map(int, input().split());
board = [];
for _ in range(n) :
    board.append(list(map(int, input().split())));
INF = int(1e9);
d = [[[-INF] * 3 for _ in range(m)] for _ in range(n)];
#0은 북에서 1은 서에서 2는 동에서
d[0][0][0] = board[0][0];
d[0][0][2] = board[0][0];

#맨 윗줄의 경우
for j in range(1, m) :
    d[0][j][1] = max(d[0][j - 1]) + board[0][j];

#그 아래부터
for i in range(1, n) :
    for j in range(0, m) :
        d[i][j][0] = max(d[i - 1][j]) + board[i][j];
    for j in range(1, m) :
        d[i][j][1] = max(d[i][j - 1]) + board[i][j];
    for j in range(m - 2, -1, -1) :
        d[i][j][2] = max(d[i][j + 1][0], d[i][j + 1][2]) + board[i][j];

print(max(d[n - 1][m - 1]));