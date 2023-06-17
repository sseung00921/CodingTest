import sys;
input = sys.stdin.readline;
from collections import deque;
sys.setrecursionlimit(10**5 + 10);

N, K = map(int, input().split());
StrToIdxMapper = dict();
IdxToStrMapper = dict();
for i in range(1, N + 1) :
    s = input().rstrip();
    StrToIdxMapper[s] = i;
    IdxToStrMapper[i] = s;
M = int(input());
EndArr = [];
for _ in range(M) :
    EndArr.append(int(input()));

Parents = [-1] * (N + 1);
Parents[1] = 1;
def dfs(now) :
    nowStr = IdxToStrMapper[now];
    for k in range(K) :
        nowStrList = list(nowStr);
        nowStrList[k] = str((int(nowStrList[k]) + 1) % 2);
        nextStr = "".join(nowStrList);
        if nextStr not in StrToIdxMapper :
            continue;
        next = StrToIdxMapper[nextStr];
        if Parents[next] != -1 :
            continue;
        Parents[next] = now;
        dfs(next);
    return;

def traceAndMakePath(endIdx) :
    rtnArr = deque([]);
    while endIdx != 1 :
        rtnArr.appendleft(endIdx);
        endIdx = Parents[endIdx];
    rtnArr.appendleft(1);
    return rtnArr;

Start = 1;
dfs(Start);

for endIdx in EndArr :
    if Parents[endIdx] == -1 :
        print(-1);
    else :
        print(*traceAndMakePath(endIdx));