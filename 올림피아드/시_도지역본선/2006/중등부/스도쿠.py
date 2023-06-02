import sys;
input = sys.stdin.readline;

Board = [];
for _ in range(9) :
    Board.append(list(map(int, input().split())));

ZeroPoses = [];
for r in range(9) :
    for c in range(9) :
        if Board[r][c] == 0 :
            ZeroPoses.append((r, c));
def checkIfClear() :
    cnt = 0;
    for i in range(9) :
        cnt += Board[i].count(0);
    if cnt == 0 :
        return True;
    return False;

def checkCondition(r, c, val) :
    arr = Board[r];
    if val in arr :
        return False;

    arr = [];
    for i in range(9) :
        arr.append(Board[i][c]);
    if val in arr :
        return False;

    arr = [];
    sr = (r // 3) * 3;
    sc = (c // 3) * 3;
    for i in range(sr, sr + 3) :
        for j in range(sc, sc + 3) :
            arr.append(Board[i][j]);
    if val in arr :
        return False;

    return True;


IsDone = False;
def dfs(idx) :
    global IsDone

    if IsDone :
        return;

    if idx == len(ZeroPoses) :
        for i in range(len(Board)) :
            print(*Board[i]);
        IsDone = True;
        return;

    r, c = ZeroPoses[idx];
    for val in range(1, 10) :
        if checkCondition(r, c, val) :
            Board[r][c] = val;
            dfs(idx + 1);
            Board[r][c] = 0;

dfs(0);
