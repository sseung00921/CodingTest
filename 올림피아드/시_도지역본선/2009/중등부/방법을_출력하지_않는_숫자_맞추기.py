import sys;
input = sys.stdin.readline;
sys.setrecursionlimit(10**6);

N = int(input());
Given = input().rstrip();
Target = input().rstrip();

d = [[-1] * 11 for _ in range(N + 1)];

def dfs(idx, turn) :
    if d[idx][turn] != -1 :
        return d[idx][turn];

    if idx == N :
        return 0;

    targetNum = int(Target[idx]);
    givenNum = int(Given[idx]);
    turnLeftCnt = (targetNum - givenNum - turn + 20) % 10;
    turnRightCnt = 10 - turnLeftCnt;

    tmp = min(dfs(idx + 1, (turn + turnLeftCnt) % 10) + turnLeftCnt,
              dfs(idx + 1, turn) + turnRightCnt);
    d[idx][turn] = tmp;
    return d[idx][turn];

print(dfs(0, 0));