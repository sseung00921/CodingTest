import sys;
input = sys.stdin.readline;

n, m = map(int, input().split());
Board = [];
Board.append([0] * (n + 1));
for _ in range(n) :
    added = [0]
    data = list(map(int, input().split()));
    added = added + data;
    Board.append(added);

for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        Board[i][j] = Board[i][j] + Board[i][j - 1];

for j in range(1, n + 1) :
    for i in range(1, n + 1) :
        Board[i][j] = Board[i][j] + Board[i - 1][j];

for _ in range(m) :
    sx, sy, ex, ey = map(int, input().split());
    answer = Board[ex][ey] - Board[sx - 1][ey] - Board[ex][sy - 1] + Board[sx - 1][sy - 1];
    print(answer)