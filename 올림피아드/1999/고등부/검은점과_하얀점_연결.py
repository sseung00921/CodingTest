import sys;
input = sys.stdin.readline;

n = int(input());
strr = list(input().rstrip());

dVal = [[-1] * n for _ in range(n)];
dH = [[0] * n for _ in range(n)];
dE = [[-1] * n for _ in range(n)];

def dfs(start, end) :
    if start > end :
        return 0;

    if dVal[start][end] != -1 :
        return dVal[start][end];

    dVal[start][end] = int(1e9);
    for middle in range(start + 1, end + 1, 2) :
        if strr[start] != strr[middle] :
            innerVal = dfs(start + 1, middle - 1);
            outerVal = dfs(middle + 1, end);
            dist = middle - start;
            height = dH[start + 1][middle - 1] + 1;
            val = 2*height + dist + innerVal + outerVal;
            if val < dVal[start][end] :
                dVal[start][end] = val;
                dH[start][end] = max(height, 0 if middle + 1 > end - 1 else dH[middle + 1][end]);
                dE[start][end] = middle;

    return dVal[start][end];

def trace(start, end) :
    if start > end :
        return;
    middle = dE[start][end];
    pairList.append((start + 1, middle + 1));
    trace(start + 1, middle - 1);
    trace(middle + 1, end);

print(dfs(0, n - 1));
pairList = [];
trace(0, n - 1);
for pair in pairList :
    print(*pair);