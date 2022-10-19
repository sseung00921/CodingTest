import sys;
Input = sys.stdin.readline;

n, m = map(int, input().split());
poses = [];
edges = [];

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def calDistance(i, j) :
    x1, y1 = poses[i];
    x2, y2 = poses[j];
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2);

for _ in range(n) :
    x, y = map(int, input().split());
    poses.append((x, y));

for _ in range(m) :
    a, b = map(int, input().split())
    edges.append((0, a, b));

for i in range(n) :
    for j in range(n) :
        edges.append((calDistance(i, j), i + 1, j + 1));
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

edges.sort();

sum = 0;
for edge in edges :
    cost, a, b = edge;
    if find_parent(parent, a) == find_parent(parent, b) :
        continue;
    else:
        union_parent(parent, a, b);
        sum += cost;

print(f'{round(sum,2):.2f}')