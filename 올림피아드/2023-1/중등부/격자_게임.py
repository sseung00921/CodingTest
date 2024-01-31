import sys;
input = sys.stdin.readline;

N, M, K = map(int, input().split());
Board = [[0] * (M + 1)];
for _ in range(N) :
    Board.append([0] + list(input().rstrip()));

Q = int(input());
Quries = [];
for _ in range(Q) :
    x, y = map(int, input().split());
    Quries.append((x, y));

d = [[[None] * 2 for _ in range(M + 1)] for _ in range(N + 1)];
CanWinSet = set();
CanWinSet.add((N - 1, M));
CanWinSet.add((N, M - 1));
for i in range(1, K + 1) :
    CanWinSet.add((N - i, M - i));

def oob(x, y) :
    if x <= 0 or x > N or y <= 0 or y > M :
        return True;
    return False;

def dfs(nowWho, nowX, nowY) :
    if (nowX, nowY) in CanWinSet :
        d[nowX][nowY][nowWho] = nowWho;
        return d[nowX][nowY][nowWho];

    if d[nowX][nowY][nowWho] != None :
        return d[nowX][nowY][nowWho];

    d[nowX][nowY][nowWho] = -1;
    opponent = (nowWho + 1) % 2;
    if (not oob(nowX + 1, nowY)) and Board[nowX + 1][nowY] == '.' :
        if dfs(opponent, nowX + 1, nowY) == nowWho :
            d[nowX][nowY][nowWho] = nowWho;
            return nowWho;
    if (not oob(nowX, nowY + 1)) and Board[nowX][nowY + 1] == '.' :
        if dfs(opponent, nowX, nowY + 1) == nowWho :
            d[nowX][nowY][nowWho] = nowWho;
            return nowWho;
    for i in range(K, 0, -1) :
        if (not oob(nowX + i, nowY + i)) and Board[nowX + i][nowY + i] == '.':
            if dfs(opponent, nowX + i, nowY + i) == nowWho:
                d[nowX][nowY][nowWho] = nowWho;
                return nowWho;


    d[nowX][nowY][nowWho] = opponent;
    return opponent;


for e in Quries :
    x, y = e;
    rst = dfs(0, x, y);
    if rst == 0 :
        print("First");
    else :
        print("Second");