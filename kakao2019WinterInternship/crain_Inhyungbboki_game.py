def pull(row, board) :
    n = len(board);
    for i in range(0, n) :
        if board[i][row] == 0 :
            continue;
        else :
            rtn = board[i][row];
            board[i][row] = 0;
            return rtn;
    return 0;

def solution(board, moves):
    answer = 0
    result = [];
    for ins in moves :
        ins -= 1;
        rtn = pull(ins, board);
        if rtn != 0 :
            result.append(rtn);
        n = len(result);
        if n >= 2 and result[n - 1] == result[n - 2] :
            answer += 2;
            result.pop();
            result.pop();

    return answer