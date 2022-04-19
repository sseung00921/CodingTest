def formatBinaryNum(binaryStr, n) :
    binaryStr = binaryStr[2:];
    if len(binaryStr) == n :
        return binaryStr;
    else :
        str = '';
        for i in range(n - len(binaryStr)) :
            str += '0';
        formatted = str + binaryStr;
        return formatted;

def makeTwoDimensionBoard(arr, n) :
    board = [[0] * n for _ in range(n)];
    for i in range(n) :
        str = formatBinaryNum(bin(arr[i]), n);
        for j in range(n) :
            board[i][j] = str[j];
    return board;


def checkIfWall(board1, board2, n) :
    rtnList = [];
    for i in range(n) :
        str = '';
        for j in range(n) :
            if board1[i][j] == '1' or board2[i][j] == '1' :
                str += '#';
            else :
                str += ' ';
        rtnList.append(str);
    return rtnList;

def solution(n, arr1, arr2):
    board1 = makeTwoDimensionBoard(arr1, n);
    board2 = makeTwoDimensionBoard(arr2, n);
    answer = checkIfWall(board1, board2, n);
    return answer

n = 5;
arr1 = [9, 20, 28, 18, 11];
arr2 = [30, 1, 21, 17, 28];
print(solution(n, arr1, arr2));