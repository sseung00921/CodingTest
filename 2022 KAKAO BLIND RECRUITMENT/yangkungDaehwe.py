maxDiff = 0;
strategies = [];

def formatBin(str) :
    str = str[2 : ];
    if len(str) < 11 :
        for i in range(11 - len(str)) :
            str = '0' + str;
    return str;

def calDiff(table, info) :
    lionScore = 0;
    apichSocre = 0;
    for i in range(11) :
        if table & (1 << (10 - i)) > 0 :
            lionScore += (10 - i);
        else :
            if info[i] > 0 :
                apichSocre += (10 - i);
    return lionScore - apichSocre;

def dfs(n, info, level, table) :
    global maxDiff;
    if level == 11 :
        diff = calDiff(table, info);
        if diff > maxDiff :
            maxDiff = diff;
            strategies.clear();
            strategies.append(formatBin(bin(table)));
        elif diff == maxDiff :
            strategies.append(formatBin(bin(table)));
        return;

    dfs(n, info, level + 1, table);
    if n > info[level] :
        dfs(n - (info[level] + 1), info, level + 1, table | (1 << (10 - level)))

def solution(n, info):
    answer = []
    dfs(n, info, 0, 0);
    if maxDiff == 0 :
        return [-1];
    for strategy in strategies :
        arrowCnt = n;
        candidate = [];
        for i in range(11) :
            if strategy[i] == '0' :
                candidate.append(0);
            else :
                candidate.append(info[i] + 1);
                arrowCnt -= (info[i] + 1);
        candidate[-1] += arrowCnt;
        answer.append(candidate);
    answer.sort(key = lambda x : x[::-1], reverse = True);
    return answer[0]


n = 5;
info = [2,1,1,1,0,0,0,0,0,0,0];
print(solution(n, info));