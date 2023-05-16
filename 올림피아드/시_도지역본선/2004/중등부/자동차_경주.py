import sys;
input = sys.stdin.readline;

n = int(input());
m = int(input());
Graph = [[] for _ in range(n + 1)];
Prev = [-1] * (n + 1);
Indegree = [0] * (n + 1);
d = [0] * (n + 1);
for _ in range(m) :
    p, q, r = map(int, input().split());
    if p == 1 :
        d[q] = r; Prev[q] = 1;
    else :
        Graph[p].append((r, q));
        Indegree[q] += 1;

def runOneCycle() :
    isAllChecked = True;
    for i in range(1, n + 1) :
        if Indegree[i] != 0 :
            continue;
        isAllChecked = False;
        for j in Graph[i] :
            score, nextNode = j;
            if d[nextNode] < d[i] + score :
                d[nextNode] = d[i] + score;
                Prev[nextNode] = i;
            Indegree[nextNode] -= 1;
        Indegree[i] = -1;

    return isAllChecked;

while True :
    isAllChecked = runOneCycle();
    if isAllChecked :
        break;

print(d[1]);
path = [1];
nowNode = 1;
while Prev[nowNode] != 1 :
    path.append(Prev[nowNode]);
    nowNode = Prev[nowNode];
path.append(Prev[nowNode]);
path.reverse();
print(*path);

