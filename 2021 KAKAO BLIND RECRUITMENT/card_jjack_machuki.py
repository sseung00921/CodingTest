from collections import deque;

Board = [];
AllRemoved = 1;
CardPairDic = {};
minManuvalCnt = int(1e9);
dr = [0, 1, 0, -1];
dc = [-1, 0, 1, 0];

def move(removed, src, desc, cost) :
    visited = [[False] * 4 for _ in range(4)];
    q = deque([(src[0], src[1], cost)]);
    while q :
        r, c, cost = q.popleft();
        if r == desc[0] and c == desc[1] :
            return cost;
        for dir in range(4) :
            nr = r + dr[dir];
            nc = c + dc[dir];
            if nr < 0 or nr > 3 or nc < 0 or nc > 3 :
                continue;
            if not visited[nr][nc] :
                visited[nr][nc] = True;
                q.append((nr, nc, cost + 1));
            for j in range(2) :
                if removed & (1 << Board[nr][nc]) == 0 :
                    break;
                if nr + dr[dir] < 0 or nr + dr[dir] > 3 or nc + dc[dir] < 0 or nc + dc[dir] > 3 :
                    break;
                nr += dr[dir];
                nc += dc[dir];
            if not visited[nr][nc] :
                visited[nr][nc] = True;
                q.append((nr, nc, cost + 1));
    return int(1e9);

def dfs(maneuvalCnt, removed, src) :
    global minManuvalCnt;
    #print(removed);
    if maneuvalCnt > minManuvalCnt :
        return;

    if removed == AllRemoved :
        minManuvalCnt = min(minManuvalCnt, maneuvalCnt);
        return;

    for num, pos in CardPairDic.items() :
        if removed & (1 << num) > 0 :
            continue;

        caseOne = move(removed, src, pos[0], 0) + move(removed, pos[0], pos[1], 0) + 2;
        caseTwo = move(removed, src, pos[1], 0) + move(removed, pos[1], pos[0], 0) + 2;

        dfs(maneuvalCnt + caseOne, removed | (1 << num), pos[1]);
        dfs(maneuvalCnt + caseTwo, removed | (1 << num), pos[0]);

def solution(board, r, c):
    global Board;
    global AllRemoved;
    global CardPairDic;
    Board = board;
    for i in range(4) :
        for j in range(4) :
            num = Board[i][j];
            if num != 0 :
                AllRemoved |= (1 << num)
                if num not in CardPairDic :
                    CardPairDic[num] = [(i, j)];
                else :
                    CardPairDic[num].append((i, j));

    dfs(0, 1, (r, c))

    return minManuvalCnt;

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]];
r = 1;
c = 0;
print(solution(board, r, c));