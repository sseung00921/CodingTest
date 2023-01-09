import sys;
input = sys.stdin.readline;
import heapq;

dr = [-1,0,1,0];
dc = [0,-1,0,1];

n = int(input());
board = [];
visited = [[False] * n for _ in range(n)];
for _ in range(n) :
    board.append(input());

q = [];
heapq.heappush(q, [0, 0, 0]);
visited[0][0] = True;
while q :
    breakCnt, r, c= heapq.heappop(q);
    if r == n - 1 and c == n - 1 :
        print(breakCnt);
        break;
    for dir in range(4) :
        nr = r + dr[dir];
        nc = c + dc[dir];
        if nr < 0 or nr >= n or nc < 0 or nc >= n :
            continue;
        if visited[nr][nc] :
            continue;
        if board[nr][nc] == '0' :
            heapq.heappush(q, (breakCnt + 1, nr, nc));
            visited[nr][nc] = True;
        else :
            heapq.heappush(q, (breakCnt, nr, nc));
            visited[nr][nc] = True;