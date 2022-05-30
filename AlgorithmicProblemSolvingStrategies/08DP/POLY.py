Mod = 10000000;
N = 0;
Cache = None;
tc = int(input());

def dfs(totalNum, firstRowNum) :
    if totalNum == firstRowNum :
        return 1;
    if Cache[totalNum][firstRowNum] != -1 :
        return Cache[totalNum][firstRowNum];

    ret = 0;
    for nextFirstRowNum in range(1, totalNum - firstRowNum + 1) :
        ret += ((firstRowNum + nextFirstRowNum - 1)*dfs(totalNum - firstRowNum, nextFirstRowNum));
        ret %= Mod;

    Cache[totalNum][firstRowNum] = ret;
    return ret;

Cache = [[-1] * 101 for _ in range(101)];
while tc > 0 :
    N = int(input());
    answer = 0;
    for i in range(1, N + 1) :
        answer += dfs(N, i);
        answer %= Mod;
    print(answer);
    tc -= 1;