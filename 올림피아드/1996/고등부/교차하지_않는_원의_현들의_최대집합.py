import sys;
input = sys.stdin.readline;

n = int(input());
lineInfo = [];
for _ in range(n) :
    s, e = map(int, input().split());
    lineInfo.append((min(s, e), max(s, e)));

lineInfo.sort();
print(lineInfo)
d = [[-1] * 2 for _ in range(n)];

def dfs(idx, isContain) :
    s, e = lineInfo[idx];

    if idx == len(lineInfo) - 1 :
        d[idx][isContain] = 0 if isContain == 0 else 1;
        return d[idx][isContain];

    if d[idx][isContain] != -1 :
        return d[idx][isContain];

    if isContain == 0 :
        d[idx][isContain] = max(dfs(idx + 1, 0), dfs(idx + 1, 1));
        return d[idx][isContain];
    elif isContain == 1 :
        maxCnt = 0;
        for next in range(idx + 1, len(lineInfo)) :
            nextS, nextE = lineInfo[next];
            if nextE > e :
                continue;
            maxCnt = max(maxCnt, dfs(next, 1));
        d[idx][isContain] = maxCnt + 1;
        return d[idx][isContain];

print(max(dfs(0, 0), dfs(0, 1)));
print(d)