import sys;
input = sys.stdin.readline;
sys.setrecursionlimit(10**4);

INF = int(1e9);
N, K = map(int, input().split());
Board = [];
for _ in range(N) :
    Board.append(list(map(int, input().split())));

dx = [0, -1, 0, 1]; #동북서남
dy = [1, 0, -1, 0];
CanGo = [[1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]];
NextDirMap = [[-1, 0, 3, -1], [3, 2, -1, -1], [-1, -1, 1, 0], [1, -1, -1, 2], [-1, 1, -1, 3], [0, -1, 2, -1]]

def oob(x, y) :
    if x < 0 or x >= N or y < 0 or y >= N :
        return True;
    return False;

def testRoute(x, y, dir) :
    if x == 0 and y == 0 :
        if Board[x][y] == 0 or Board[x][y] == 2 or Board[x][y] == 3 or Board[x][y] == 4 :
            return -1

    dist = 1;
    while True :
        if x == N - 1 and y == N - 1 :
            if Board[x][y] == 2 or Board[x][y] == 5 :
                return dist;
            else:
                return -1

        dir = NextDirMap[Board[x][y]][dir]
        x = x + dx[dir];
        y = y + dy[dir];
        if oob(x, y) :
            return -1;
        if not CanGo[Board[x][y]][(dir + 2) % 4] :
            return -1;
        dist += 1;

if K == 0 :
    answer = testRoute(0, 0, 0);
    print(answer);
elif K == 1 :
    Answer = INF;
    for i in range(0, N) :
        for j in range(0, N) :
            oriVal = Board[i][j];
            for k in range(0, 6) :
                if k == oriVal :
                    continue;
                Board[i][j] = k;
                answer = testRoute(0, 0, 0);
                if answer != -1 :
                    Answer = min(Answer, answer);
            Board[i][j] = oriVal;
    if Answer == INF :
        Answer = -1;
    print(Answer);