tc = int(input());
DATA = None;
N = 0;
def dfs(left, right) :
    if left == right :
        return DATA[left];

    mid = (left + right) // 2;
    rtnVal = max(dfs(left, mid) , dfs(mid + 1, right));

    lo = mid; hi = mid + 1;
    hForMaxM = min(DATA[lo], DATA[hi]);
    wForMaxM = 2;
    maxM = hForMaxM * wForMaxM;
    while left < lo or hi < right :
        if lo > left and (hi == right or DATA[lo - 1] > DATA[hi + 1]) :
            hForMaxM = min(hForMaxM, DATA[lo - 1]);
            lo -= 1;
        else :
            hForMaxM = min(hForMaxM, DATA[hi + 1]);
            hi += 1;
        maxM = max(maxM, hForMaxM * (hi - lo + 1));
    rtnVal = max(rtnVal, maxM);
    return rtnVal;


while tc > 0 :
    n = int(input());
    N = n;
    data = list(map(int, input().split()));
    DATA = data;
    print(dfs(0, n - 1));
    tc -= 1;