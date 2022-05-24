tc = int(input());
N = 0;
ARE_FRIENDS = None;

def dfs(isTaken) :
    firstFree = -1;
    for i in range(len(isTaken)) :
        if isTaken[i] == False :
            firstFree = i;
            break;
    if firstFree == -1 :
        return 1;
    cnt = 0;
    for i in range(firstFree + 1, N) :
        if isTaken[i] == False and ARE_FRIENDS[firstFree][i] == True :
            isTaken[firstFree] = True;
            isTaken[i] = True;
            cnt += dfs(isTaken);
            isTaken[i] = False;
            isTaken[firstFree] = False;
    return cnt;

while tc > 0 :
    n, m = map(int, input().split());
    N = n;
    ARE_FRIENDS = [[False] * n for _ in range(n)];
    data = list(map(int, input().split()));
    for i in range(0, len(data) - 1, 2) :
        ARE_FRIENDS[data[i]][data[i + 1]] = True;
        ARE_FRIENDS[data[i + 1]][data[i]] = True;
    isTaken = [False] * n;
    print(dfs(isTaken));
    tc -= 1;
