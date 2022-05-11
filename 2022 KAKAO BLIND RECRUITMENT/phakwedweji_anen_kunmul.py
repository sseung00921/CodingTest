def solution(board, skill):
    N = len(board);
    M = len(board[0]);
    d = [[0] * (M + 1) for _ in range(N + 1)]
    for s in skill :
        d[s[1]][s[2]] += s[5] if s[0] == 2 else -s[5];
        d[s[1]][s[4] + 1] += -s[5] if s[0] == 2 else s[5];
        d[s[3] + 1][s[2]] += -s[5] if s[0] == 2 else s[5];
        d[s[3] + 1][s[4] + 1] += s[5] if s[0] == 2 else -s[5];
    answer = 0

    for i in range(N) :
        for j in range(M) :
            d[i][j + 1] += d[i][j];

    for j in range(M) :
        for i in range(N) :
            d[i + 1][j] += d[i][j];

    for i in range(N) :
        for j in range(M) :
            board[i][j] += d[i][j];
            if board[i][j] > 0 :
                answer += 1;

    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]];
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]];
print(solution(board, skill));