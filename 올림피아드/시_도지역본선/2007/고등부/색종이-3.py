import sys;
input = sys.stdin.readline;

Board = [[0] * 101 for _ in range(101)];
N = int(input());
Events = [];

def prettyPrintBoard() :
    for e in Board :
        print(*e);

for _ in range(N) :
    sx, sy = map(int, input().split());
    ex = sx + 10;
    ey = sy + 10;
    for i in range(sx, ex) :
        for j in range(sy, ey) :
            Board[i][j] = 1;

for j in range(0, 100) :
    for i in range(0, 99) :
        if Board[i][j] != 0 and Board[i + 1][j] != 0 :
            Board[i + 1][j] = Board[i][j] + 1;

Answer = 0;
for i in range(0, 100) :
    for j in range(0, 100) :
        h = 100;
        if Board[i][j] == 0 :
            continue;
        for k in range(j, 100) :
            if Board[i][k] == 0 :
                break;
            h = min(h, Board[i][k]);
            Answer = max(Answer, h * (k - j + 1));

print(Answer);






