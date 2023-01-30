import sys;
input = sys.stdin.readline;

n = int(input());
chus = list(map(int, input().split()));
m = int(input());
checks = list(map(int, input().split()));

d = [[False] * 30001 for _ in range(n + 1)];
d2 = [False] * 30001;

def dfs(covered, diff) :
    if covered == n :
        d[covered][diff] = True;
        d2[diff] = True;
        return;
    if d[covered][diff] == True :
        return;

    d[covered][diff] = True;
    d2[diff] = True;
    dfs(covered + 1, diff) #안 올림
    dfs(covered + 1, diff - chus[covered]) #왼 쪽에 올림
    dfs(covered + 1, diff + chus[covered]) #오른 쪽에 올림

dfs(0, 15000);
answer = [];
for check in checks :
    if check <= 15000 and d2[check + 15000] == True :
        answer.append("Y");
    else :
        answer.append("N");

print(*answer);