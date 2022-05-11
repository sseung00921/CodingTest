dr = [-1,0,1,0];
dc = [0,1,0,-1];
n = 0;
m = 0;
Board = [[0] * 5 for _ in range(5)];
visited = [[0] * 5 for _ in range(5)];

def oob(r, c) :
    if r < 0 or r >= n or c < 0 or c >= m :
        return True;
    return False;

def dfs(curr, curc, opr, opc) :
    if visited[curr][curc] == 1 :
        return 0;

    rtn = 0;
    for dir in range(4) :
        nr = curr + dr[dir];
        nc = curc + dc[dir];
        if oob(nr, nc) == False and Board[nr][nc] != 0 and visited[nr][nc] == False:
            visited[curr][curc] = 1;
            val = dfs(opr, opc, nr, nc) + 1;
            visited[curr][curc] = 0;

            if rtn % 2 == 0 and val % 2 == 1 :
                rtn = val;
            elif rtn % 2 == 1 and val % 2 == 1 :
                rtn = min(rtn, val);
            elif rtn % 2 == 0 and val % 2 == 0 :
                rtn = max(rtn, val);

    return rtn;


def solution(board, aloc, bloc):
    global n;
    global m;
    n = len(board);
    m = len(board[0]);
    for i in range(n) :
        for j in range(m) :
            Board[i][j] = board[i][j];
    return dfs(aloc[0], aloc[1], bloc[0], bloc[1]);

board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]];
aloc = [1, 0];
bloc = [1, 2];
print(solution(board, aloc, bloc));