from collections import deque;

n = int(input());
d = [0] * (n + 1);
times = [0] * (n + 1);
degree = [0] * (n + 1);
graph = [[] for _ in range(n + 1)];
for i in range(n) :
    data = list(map(int, input().split()));
    times[i + 1] = data[0];
    d[i + 1] = data[0];
    for j in range(1, len(data)) :
        if data[j] == -1 :
            break;
        graph[data[j]].append(i + 1);
        degree[i + 1] += 1;

q = deque([])
for i in range(1, n + 1) :
    if degree[i] == 0 :
        q.append((i));

while q :
    now = q.popleft();
    for i in graph[now] :
        d[i] = max(d[i], d[now] + times[i]);
        degree[i] -= 1;
        if degree[i] == 0 :
            q.append(i);

for i in range(1, n + 1) :
    print(d[i]);

#5
#10 -1
#10 1 -1
#4 1 -1
#4 3 1 -1
#3 3 -1