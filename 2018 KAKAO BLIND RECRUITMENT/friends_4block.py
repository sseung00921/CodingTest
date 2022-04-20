import copy;

def decideToDel(m, n, board, delCheckBoard) :
    for i in range(m - 1) :
        for j in range(n - 1) :
            if board[i][j] == '0' :
                continue;
            if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] :
                delCheckBoard[i][j] = True;
                delCheckBoard[i + 1][j] = True;
                delCheckBoard[i][j + 1] = True;
                delCheckBoard[i + 1][j + 1] = True;
    return;

def delete(m, n, board, delCheckBoard) :
    cnt = 0;
    for i in range(m) :
        for j in range(n) :
            if delCheckBoard[i][j] == True :
                board[i][j] = '0';
                cnt += 1;
    return cnt;

def moveBoard(m, n, board) :
    for j in range(n) :
        while True :
            movableExist = False;
            for i in range(1, m) :
                if board[i][j] == '0' and board[i - 1][j] != '0':
                    movableExist = True;
                    board[i - 1][j], board[i][j] = board[i][j], board[i - 1][j];
            if movableExist == False :
                break;

def solution(m, n, board):
    answer = 0
    twoDBoard = [[None] * n for _ in range(m)];
    delCheckBoard = [[False] * n for _ in range(m)];

    for i in range(m) :
        str = board[i];
        for j in range(n) :
            twoDBoard[i][j] = str[j];
    board = twoDBoard;

    while True :
        tDelCheckBoard = copy.deepcopy(delCheckBoard);
        decideToDel(m, n, board, tDelCheckBoard);
        delCnt = delete(m, n, board, tDelCheckBoard);
        if delCnt == 0 :
            break;
        answer += delCnt;
        moveBoard(m, n, board);
    return answer

m = 4;
n = 5;
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"];
print(solution(m, n, board));