import sys;
from collections import deque;

input = sys.stdin.readline;
N = int(input());
Likes = [[] for _ in range(N + 1)];
Board = [];
for _ in range(N) :
    Board.append(list(map(int, input().split())));
for i in range(N) :
    for j in range(N) :
        if Board[i][j] == 0 and Board[j][i] == 0:
            Likes[i + 1].append(j + 1);
            Likes[j + 1].append(i + 1);

Visited = [0] * (N + 1);
Groups = [];

def bfs(num) :
    group = [num];
    q = deque([num]);
    Visited[num] = 1;

    while q :
        now  = q.popleft();
        for next in Likes[now] :
            if Visited[next] == 1 :
                continue;
            q.append(next);
            Visited[next] = 1;
            group.append(next);

    return group;

for i in range(1, N + 1) :
    if Visited[i] == 1 :
        continue;
    tmpArr = bfs(i);
    Groups.append(tmpArr);

for sGroup in Groups :
    if len(sGroup) == 1 :
        print(0);
        sys.exit();

GroupNumArr = [-1] * (N + 1);
for i in range(1, N + 1) :
    for j in range(len(Groups)) :
        if i in Groups[j] :
            GroupNumArr[i] = j;
            break;

for i in range(N) :
    for j in range(N) :
        if GroupNumArr[i + 1] == GroupNumArr[j + 1] :
            if Board[i][j] == 1 or Board[j][i] == 1 :
                print(0);
                sys.exit();
        else :
            if Board[i][j] == 0 or Board[j][i] == 0 :
                print(0);
                sys.exit();

for i in range(len(Groups)) :
    Groups[i].sort();

Groups.sort(key = lambda x : x[0]);
print(len(Groups));
for sGroup in Groups :
    print(*sGroup);
