n, m = map(int, input().split());
parents = [0] * (n + 1);

def findParent(parents, x) :
    if parents[x] != x :
        parents[x] = findParent(parents, parents[x]);
    return parents[x];

def unionParent(parents, a, b) :
    a = findParent(parents, a);
    b = findParent(parents, b);
    if b < a :
        parents[a] = b;
    else:
        parents[b] = a;

for i in range(n + 1) :
    parents[i] = i;

for _ in range(m) :
    cmd, a, b = map(int, input().split());
    if cmd == 0 :
        unionParent(parents, a, b);
    elif cmd == 1 :
        if findParent(parents, a) == findParent(parents, b) :
            print("YES");
        else :
            print("NO");