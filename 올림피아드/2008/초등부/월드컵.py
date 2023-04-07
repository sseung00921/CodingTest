import sys;
input = sys.stdin.readline;
from itertools import combinations;

matchList = list(combinations([0, 1, 2, 3, 4, 5], 2));

def dfs(matchIdx) :
    global isPossible;

    if isPossible == 1 :
        return;

    if matchIdx == 15 :
        for i in range(6) :
            if record[i].count(0) != 3 :
                return;
        isPossible = 1;
        return;

    t1 = matchList[matchIdx][0];
    t2 = matchList[matchIdx][1];

    #t1 승
    if record[t1][0] > 0 and record[t2][2] > 0 :
        record[t1][0] -= 1;
        record[t2][2] -= 1;
        dfs(matchIdx + 1);
        record[t1][0] += 1;
        record[t2][2] += 1;
    #t2 승
    if record[t1][2] > 0 and record[t2][0] > 0 :
        record[t1][2] -= 1;
        record[t2][0] -= 1;
        dfs(matchIdx + 1);
        record[t1][2] += 1;
        record[t2][0] += 1;
    #비김
    if record[t1][1] > 0 and record[t2][1] > 0 :
        record[t1][1] -= 1;
        record[t2][1] -= 1;
        dfs(matchIdx + 1);
        record[t1][1] += 1;
        record[t2][1] += 1;

answer = [];
isPossible = 0;
for _ in range(4) :
    data = list(map(int, input().split()))
    record = [];
    for i in range(0, 18, 3) :
        record.append(data[i : i + 3]);
    isPossible = 0;
    dfs(0);
    answer.append(isPossible);

print(*answer);



