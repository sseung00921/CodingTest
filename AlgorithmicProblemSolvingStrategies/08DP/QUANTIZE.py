INF = int(1e9);
N = 0;
S = 0;
DATA = None;
tc = int(input());
Cache = None;
preSum = None;
preSqSum = None;

def preCalc() :
    DATA.sort();
    preSum[0] = DATA[0];
    preSqSum[0] = DATA[0]*DATA[0];
    for i in range(1, N) :
        preSum[i] = preSum[i - 1] + DATA[i];
        preSqSum[i] = preSqSum[i - 1] + DATA[i]*DATA[i];

def minError(begin, end) :
    sum = preSum[end] - (0 if begin == 0 else preSum[begin - 1]);
    sqSum = preSqSum[end] - (0 if begin == 0 else preSqSum[begin - 1]);
    m = int(sum / (end - begin + 1) + 0.5);
    ret = sqSum - 2*m*sum + m*m*(end - begin + 1);
    return ret;


def dfs(begin, parts) :
    if begin == N :
        return 0;
    if parts == 0 :
        return INF;
    if Cache[begin][parts] != INF :
        return Cache[begin][parts];

    for i in range(1, N + 1) :
        if begin + i > N :
            break;
        Cache[begin][parts] = min(Cache[begin][parts], minError(begin, begin + i - 1) + dfs(begin + i, parts - 1));

    return Cache[begin][parts];

while tc > 0 :
    N, S = map(int, input().split());
    DATA = list(map(int, input().split()))
    preSum = [INF] * 101;
    preSqSum = [INF] * 101;
    Cache = [[INF] * 11 for _ in range(101)];
    preCalc();
    print(dfs(0, S));
    tc -= 1;
