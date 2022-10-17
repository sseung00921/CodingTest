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

"""아래는 구간 곱 버전이다. 위에 것에서 0을 나누는 문제를 해결하기 위한 변형이 살짝 들어갔을 뿐 거의 내용은 유사하나 참고하기 쉽도록 하기 위해 아래에 또 적어둔다."""
import sys;
Input = sys.stdin.readline;

n, m, k = map(int, Input().split());
l = [];
tree = [0] * (4 * n);
MOD = 1000000007;

def initTree(node, start, end) :
    if start == end :
        tree[node] = l[start];
        return tree[node];

    mid = (start + end)//2;
    tree[node] = (initTree(2*node, start, mid) * initTree(2*node + 1, mid + 1, end)) % MOD;
    return tree[node];

def update(node, start, end, index, diff) :
    if index < start or index > end :
        return;

    if start == end :
        tree[node] = diff;
    else :
        mid = (start + end)//2;
        update(2*node, start, mid, index, diff)
        update(2*node + 1, mid + 1, end, index, diff);
        tree[node] = tree[2*node] * tree[2*node + 1] % MOD

def subMul(node, start, end, left, right) :
    if right < start or end < left :
        return 1;

    if left <= start and end <= right :
        return tree[node];

    mid = (start + end)//2;
    return int((subMul(2*node, start, mid, left, right) * subMul(2*node + 1, mid + 1, end, left, right)) % MOD);

for _ in range(n) :
    l.append(int(Input()));

initTree(1, 0, n - 1);

for _ in range(m + k) :
    a, b, c = map(int, Input().split());
    if a == 1 :
        b -= 1;
        update(1, 0, n - 1, b, c);
    elif a == 2 :
        b -= 1;
        c -= 1;
        print(subMul(1, 0, n - 1, b, c));




