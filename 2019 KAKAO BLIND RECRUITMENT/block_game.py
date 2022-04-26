Board = [];

def canFill(row, col) :
    for i in range(row) :
        if Board[i][col] != 0 :
            return False;
    return True;

def canDelete(row, col, h, w) :
    lastValue = -1;
    canFillCnt = 0;
    alreadySameValFillCnt = 0;
    for i in range(row, row + h) :
        for j in range(col, col + w) :
            if Board[i][j] != 0 :
                if lastValue == -1 :
                    lastValue = Board[i][j];
                    alreadySameValFillCnt += 1;
                else :
                    if lastValue != Board[i][j] :
                        return False;
                    else :
                        alreadySameValFillCnt += 1;
            else :
                if canFill(i, j) == True :
                    canFillCnt += 1;
                else :
                    return False;
    if canFillCnt == 2 and alreadySameValFillCnt == 4 :
        for i in range(row, row + h) :
            for j in range(col, col + w) :
                Board[i][j] = 0;
        return True;
    return False;

def solution(board):
    global Board;
    Board = board;
    n = len(board);
    answer = 0
    while True :
        cnt = 0;
        for i in range(n) :
            for j in range(n) :
                if i < n - 1 and j < n - 2 and canDelete(i, j, 2, 3) == True :
                    cnt += 1;
                elif i < n - 2 and j < n - 1 and canDelete(i, j, 3, 2) == True :
                    cnt += 1;
        if cnt == 0 :
            break;
        answer += cnt;
    return answer;

board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]];
print(solution(board));