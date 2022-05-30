Mod = 1000000007;
N = 0;
Cache = None;

def dfs(width) :
    if width <= 1 :
        return 1;
    if Cache[width] != -1 :
        return Cache[width];
    Cache[width] = (dfs(width - 1) + dfs(width - 2)) % Mod;
    return Cache[width]

def exceptBalanced(width) :
    if width % 2 == 1 :
        return (dfs(width) - dfs(width // 2) + Mod) % Mod;
    ret = dfs(width);
    ret = (ret - dfs(width // 2) + Mod) % Mod;
    ret = (ret - dfs(width // 2 - 1) + Mod) % Mod;
    return ret;

tc = int(input());
while tc > 0 :
    N = int(input());
    Cache = [-1] * 101;
    print(exceptBalanced(N));
    tc -= 1;