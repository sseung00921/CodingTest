#DFS와 BFS를 사용하는 가장 기본적인 문제
from collections import deque;

N = 0;
GRAPH = [[0] * 1001 for _ in range(1001)]
IsVisited = 0;
DFSArr = [];
BFSArr = [];
def dfs(start) :
    global N;
    global IsVisited;
    if IsVisited == (1 << N) - 1 :
        return;
    for i in range(1, N + 1) :
        if GRAPH[start][i] == 1 and IsVisited & (1 << (i - 1)) == 0 :
            IsVisited = IsVisited | (1 << (i - 1))
            DFSArr.append(i);
            dfs(i);

def bfs(start) :
    global N;
    global IsVisited;
    q = deque([start]);
    while q :
        now = q.popleft();
        for i in range(1, N + 1) :
            if GRAPH[now][i] == 1 and IsVisited & (1 << (i - 1)) == 0 :
                IsVisited = IsVisited | (1 << (i - 1))
                BFSArr.append(i);
                q.append(i);

n, m, start = map(int, input().split());
N = n;
for _ in range(m) :
    a, b = map(int, input().split());
    GRAPH[a][b] = 1;
    GRAPH[b][a] = 1;

DFSArr.append(start);
IsVisited = IsVisited | (1 << (start - 1));
dfs(start)

#두 문제 사이에 전역변수 초기화
BFSArr.append(start);
IsVisited = 0 | (1 << (start - 1));
bfs(start)

print(*DFSArr);
print(*BFSArr);