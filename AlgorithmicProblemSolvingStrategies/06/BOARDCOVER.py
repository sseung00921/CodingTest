delta = [[[0,0],[1,0],[0,1]], [[0,0],[0,1],[1,1]], [[0,0],[1,0],[1,-1]], [[0,0],[1,0],[1,1]]];
H = 0;
W = 0;

def set(r, c, board, type, cmd) :
    rtnBool = True;
    for i in range(3) :
        nr = r + delta[type][i][0];
        nc = c + delta[type][i][1];
        if nr < 0 or nr >= H or nc < 0 or nc >= W :
            rtnBool = False;
            continue;
        board[nr][nc] += cmd;
        if board[nr][nc] > 1 :
            rtnBool = False;
    return rtnBool;

def dfs(board) :
    r = -1; c = -1;
    for i in range(H) :
        for j in range(W) :
            if board[i][j] == 0 :
                r = i; c = j;
                break;
        if c != -1 :
            break;
    if c == -1 :
        return 1;

    rtn = 0;
    for type in range(4) :
        if set(r, c, board, type, 1) :
            rtn += dfs(board);
        set(r, c, board, type, -1);
    return rtn;

def checkIfSpaceCntMod3EqualZero(board) :
    cnt = 0;
    for i in range(H) :
        for j in range(W) :
            if board[i][j] == 0 :
                cnt += 1;
    if cnt % 3 == 0 :
        return True;
    else :
        return False;

tc = int(input());
while tc > 0 :
    h, w = map(int, input().split());
    H = h; W = w;
    board = [[None] * w for _ in range(h)];
    for i in range(h) :
        data = input();
        for j in range(w) :
            if data[j] == '#' :
                board[i][j] = 1;
            else :
                board[i][j] = 0;
    if checkIfSpaceCntMod3EqualZero(board) == False :
        print(0);
        tc -= 1;
        continue;
    print(dfs(board));
    tc -= 1;