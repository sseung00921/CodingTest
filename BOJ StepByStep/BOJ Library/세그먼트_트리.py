import sys;
Input = sys.stdin.readline;

n, m, k = map(int, Input().split());
l = [];
tree = [0] * (4 * n);

def initTree(node, start, end) :
    if start == end :
        tree[node] = l[start];
        return tree[node];

    mid = (start + end)//2;
    tree[node] = initTree(2*node, start, mid) + initTree(2*node + 1, mid + 1, end);
    return tree[node];

def update(node, start, end, index, diff) :
    if index < start or index > end :
        return;

    tree[node] += diff;

    if start != end :
        mid = (start + end)//2;
        update(2*node, start, mid, index, diff)
        update(2*node + 1, mid + 1, end, index, diff);

def subSum(node, start, end, left, right) :
    if right < start or end < left :
        return 0;

    if left <= start and end <= right :
        return tree[node];

    mid = (start + end)//2;
    return subSum(2*node, start, mid, left, right) + subSum(2*node + 1, mid + 1, end, left, right);

for _ in range(n) :
    l.append(int(Input()));

initTree(1, 0, n - 1);

for _ in range(m + k) :
    a, b, c = map(int, Input().split());
    if a == 1 :
        b -= 1;
        diff = c - l[b];
        l[b] = c;
        update(1, 0, n - 1, b, diff);
    elif a == 2 :
        b -= 1;
        c -= 1;
        print(subSum(1, 0, n - 1, b, c));
