import sys;
input = sys.stdin.readline;

N = int(input());

def check(strr) :
    left = 0;
    right = len(strr) - 1;

    useChance = False;
    isNormal = False;
    needToCheckSkipRight = False;
    while True :
        if strr[left] != strr[right] :
            if not useChance :
                useChance = True;
                if strr[left + 1] == strr[right] and strr[left] == strr[right - 1] :
                    left += 1;
                    needToCheckSkipRight = True;
                elif strr[left + 1] == strr[right] :
                    left += 1;
                elif strr[left] == strr[right - 1] :
                    right -= 1;
                else :
                    isNormal = True;
                    break;
            else:
                isNormal = True;
                break;
        left += 1;
        right -= 1;
        if left >= right :
            break;
    if not useChance :
        return 0;
    if useChance and not isNormal :
        return 1;
    if isNormal and needToCheckSkipRight :
        left = 0;
        right = len(strr) - 1;
        useChance = False;
        isNormal = False;
        while True :
            if strr[left] != strr[right] :
                if not useChance :
                    right -= 1;
                    useChance = True;
                else :
                    isNormal = True;
                    break;
            left += 1;
            right -= 1;
            if left >= right :
                break;
        if useChance and not isNormal :
            return 1;
    return 2;

for _ in range(N) :
    strr = input().rstrip();
    print(check(strr));
