import sys;
input = sys.stdin.readline;
N = int(input());

def inbound(r, c) :
    if 0 <= r < N and 0 <= c < N :
        return True;
    return False;

Board = [];
for _ in range(N) :
    Board.append(list(map(int, input().split())));

rd = dict();
for i in range(-N + 1, N) :
    rd[i] = 0;

Answer = 0;

def calCntPossible(diag) :
    cnt = 0;
    for d in range(diag, 2*N) :
        for y in range(d + 1) :
            x = d - y;
            if inbound(x, y) and Board[x][y] and rd[x - y] == 0 :
                cnt += 1;
                break;
    return cnt;

def dfs(diag, cnt) :
    global Answer;

    if diag == 2*N :
        Answer = max(Answer, cnt);
        return;

    if cnt + calCntPossible(diag) <= Answer :
        return;

    for y in range(diag + 1) :
        x = diag - y;
        if inbound(x, y) and Board[x][y] and rd[x - y] == 0 :
            rd[x - y] = 1;
            dfs(diag + 1, cnt + 1);
            rd[x - y] = 0;
    dfs(diag + 1, cnt);


dfs(0, 0);
print(Answer);