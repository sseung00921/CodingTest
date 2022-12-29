import sys;
input = sys.stdin.readline;

n = int(input());
mapper = dict();

idx = 1;
for _ in range(n) :
    mapper[idx] = int(input());
    idx += 1;

visited = [0] * (n + 1);

def dfs(startNum) :
    tracked = [startNum];
    nowNum = startNum
    while True :
        nextNum = mapper[nowNum];
        if nextNum in tracked and nextNum == startNum :
            for e in tracked :
                visited[e] = 1;
                return;
        elif nextNum in tracked and nextNum != startNum :
            return;
        tracked.append(nextNum);
        nowNum = nextNum;

for idx in range(1, n + 1) :
    if visited[idx] == 1 :
        continue;
    dfs(idx);

answerCnt = 0;
answerArr = [];
for idx in range(1, n + 1) :
    if visited[idx] == 1 :
        answerCnt += 1;
        answerArr.append(idx);

print(answerCnt);
for e in answerArr :
    print(e);