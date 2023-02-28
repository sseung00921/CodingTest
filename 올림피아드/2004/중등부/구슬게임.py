import sys;
input = sys.stdin.readline;
sys.setrecursionlimit(10**6);

choices = list(map(int, input().split()));
data = [];
d = [[[-1] * 501 for _ in range(501)] for _ in range(2)];

for _ in range(5) :
    data.append(list(map(int, input().split())));

def dfs(who, oneRemain, twoRemain) :
    next = 0 if who == 1 else 1;
    if oneRemain < min(choices) and twoRemain < min(choices) :
        d[who][oneRemain][twoRemain] = next;
        return d[who][oneRemain][twoRemain];

    if d[who][oneRemain][twoRemain] != -1 :
        return d[who][oneRemain][twoRemain];

    canWin = False;
    for choice in choices :
        if oneRemain - choice < 0 :
            continue;
        if dfs(next, oneRemain - choice, twoRemain) == who :
            canWin = True;
    for choice in choices :
        if twoRemain - choice < 0 :
            continue;
        if dfs(next, oneRemain, twoRemain - choice) == who :
            canWin = True;

    if canWin :
        d[who][oneRemain][twoRemain] = who;
        return d[who][oneRemain][twoRemain];
    else :
        d[who][oneRemain][twoRemain] = next;
        return d[who][oneRemain][twoRemain];

for i in range(5) :
    if dfs(0, data[i][0], data[i][1]) == 0:
        print("A");
    else :
        print("B");
