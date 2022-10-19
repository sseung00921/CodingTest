import sys;
Input = sys.stdin.readline;

n, m, k = map(int, Input().split());
l = [];
tree = [0] * (4 * n);
lazy = [0] * (4 * n);

def initTree(node, start, end) :
    if start == end :
        tree[node] = l[start];
        return tree[node];

    mid = (start + end)//2;
    tree[node] = initTree(2*node, start, mid) + initTree(2*node + 1, mid + 1, end);
    return tree[node];

def lazyUpdate(node, start, end) :
    if lazy[node] != 0 :
        tree[node] += (end - start + 1)*lazy[node];
        if start != end :
            lazy[2*node] += lazy[node];
            lazy[2*node + 1] += lazy[node];
        lazy[node] = 0;

def update(node, start, end, frmIdx, toIdx, diff) :
    lazyUpdate(node, start, end); #update 메서드 안에도 얘가 있는 이유는 이전에 실행한 update CMD의 영향을 반영하기 위해서이다. 딱 한번만 update를 한다면 이 구절은 필요 없다.

    if toIdx < start or frmIdx > end :
        return;

    if frmIdx <= start and end <= toIdx :
        tree[node] += (end - start + 1)*diff;
        if start != end :
            lazy[2*node] += diff;
            lazy[2*node + 1] += diff;
        return;

    if start != end :
        mid = (start + end)//2;
        update(2*node, start, mid, frmIdx, toIdx, diff)
        update(2*node + 1, mid + 1, end, frmIdx, toIdx, diff);
        tree[node] = tree[2*node] + tree[2*node + 1];

def subSum(node, start, end, left, right) :
    lazyUpdate(node, start, end);

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
    data = list(map(int, Input().split()));
    if len(data) == 4 :
        frm = data[1] - 1;
        to = data[2] - 1;
        diff = data[3];
        update(1, 0, n - 1, frm, to, diff);
    elif len(data) == 3 :
        frm = data[1] - 1;
        to = data[2] - 1;
        print(subSum(1, 0, n - 1, frm, to));