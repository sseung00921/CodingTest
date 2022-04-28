from collections import deque;

def solution(n, path, order):
    graph = [[] for _ in range(n)];
    visited = [False] * n;
    beforeThis = dict();
    for a, b in path :
        graph[a].append(b);
        graph[b].append(a);
    for pre, post in order :
        beforeThis[post] = pre;

    afterThis = dict();
    visitedCnt = 0;
    q = deque([0]);
    while q :
        now = q.popleft();
        if now in beforeThis and visited[beforeThis[now]] == False :
            afterThis[beforeThis[now]] = now;
            continue;

        visited[now] = True;
        visitedCnt += 1;

        for next in graph[now] :
            if visited[next] == False :
                q.append(next);

        if now in afterThis :
            q.append(afterThis[now]);

    if visitedCnt == n :
        return True;
    else :
        return False;

n = 9;
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]];
order = [[8,5],[6,7],[4,1]];
print(solution(n, path, order));