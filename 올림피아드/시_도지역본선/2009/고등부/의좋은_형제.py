import sys;
input = sys.stdin.readline;

N = int(input());
Board = [];
for _ in range(N) :
    Board.append(list(map(int, input().split())));

SumBoard = [[0] * 25 for _ in range(25)];
AllSum = 0;
for col in range(N) :
    for row in range(1, N + 1) :
        if row == 1 :
            SumBoard[row][col] = Board[row - 1][col];
        else :
            SumBoard[row][col] = SumBoard[row - 1][col] + Board[row - 1][col];
        AllSum += Board[row - 1][col];

d = [[[-1] * 50000 for _ in range(25)] for _ in range(25)];

def dfs(col, cnt, youngerTotal) :
    if d[col][cnt][youngerTotal] != -1 :
        return d[col][cnt][youngerTotal];

    if col == N - 1 :
        newYoungerTotal = youngerTotal + SumBoard[cnt][col];
        d[col][cnt][youngerTotal] = abs(newYoungerTotal - (AllSum - newYoungerTotal))
        return d[col][cnt][youngerTotal];

    tmp = int(1e9);
    newYoungerTotal = youngerTotal + SumBoard[cnt][col];
    for nextCnt in range(cnt, -1, -1) :
        rst = dfs(col + 1, nextCnt, newYoungerTotal);
        if rst < tmp :
            tmp = rst;
            d[col][cnt][youngerTotal] = rst;

    return d[col][cnt][youngerTotal];

tmp = int(1e9);
Answer = -1;
StartCnt = -1;
for startCnt in range(0, N + 1) :
    rst = dfs(0, startCnt, 0);
    if rst < tmp :
        tmp = rst;
        Answer = tmp;
        StartCnt = startCnt;

print(Answer);

Path = [N - StartCnt];
MinVal = Answer;
def dfs2(col, cnt, youngerTotal) :
    if col == N - 1 :
        return;

    newYoungerTotal = youngerTotal + SumBoard[cnt][col];
    for nextCnt in range(cnt, -1, -1) :
        if dfs(col + 1, nextCnt, newYoungerTotal) == MinVal :
            Path.append(N - nextCnt);
            dfs2(col + 1, nextCnt, newYoungerTotal);
            break;

dfs2(0, StartCnt, 0);
print(*Path);
