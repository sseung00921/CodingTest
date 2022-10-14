"""SCC(Strongly Connected Component) 분할 알고리즘으로는 코사리주 알고리즘과 타잔 알고리즘이 있는데 둘 다 O(V+E)의 시간복잡도이나 타잔 알고리즘이
코사리주 알고리즘의 절반정도의 시간이 걸려 살짝 더 빠르다. 그러나 알고리즘을 이해하기에는 코사리주 알고리즘이 더 쉬워 아래는 코사리주 알고리즘에 따라 SCC를 분할하는 알고리즘을
적어두었다. SCC 분할이 필요할 땐 아래를 쓰면 되겠으나 나중에 공부하다가 타잔 알고리즘이 특별히 풀이를 쉽게 해주는 사례가 있다면 그 때 타잔 알고리즘도 공부하고 정리해두도록 하자."""

import sys;
sys.setrecursionlimit(10**5);
input = sys.stdin.readline;
v, e = map(int, input().split());
fowardGraph = [[] for _ in range(v + 1)];
reverseGraph = [[] for _ in range(v + 1)];
for _ in range(e) :
    a, b = map(int, input().split());
    fowardGraph[a].append(b);
    reverseGraph[b].append(a);

visited = [False] * (v + 1);
stack = [];

def dfs(start) :
    visited[start] = True;
    for next in fowardGraph[start] :
        if not visited[next] :
            dfs(next);
    stack.append(start);

def reverseDfs(start, scc) :
    visited[start] = True;
    for next in reverseGraph[start] :
        if not visited[next] :
            reverseDfs(next, scc);
    scc.append(start);
    return scc;

for i in range(1, v + 1) :
    if not visited[i] :
        dfs(i);

visited = [False] * (v + 1);
answer = [];
while stack :
    e = stack.pop();
    scc = [];

    if visited[e] :
        continue;

    answer.append(sorted(reverseDfs(e, scc)));

print(len(answer));
answer.sort(key = lambda x : x[0]);
for scc in answer :
    print(*scc, -1);

