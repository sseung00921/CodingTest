n = int(input());
minGoodArr = -1;


def checkIfPossible(strArr) :
    for i in range(1, len(strArr) + 1) :
        if strArr[len(strArr) - i : ] == strArr[len(strArr) - (i*2) : len(strArr) - i] :
            return False;
    return True;

def dfs(strArr, n) :
    global minGoodArr;

    if not checkIfPossible(strArr) :
        return False;
    if n == 0 :
        strr = ''.join(strArr);
        num = int(strr);
        if minGoodArr == -1 :
            minGoodArr = num;
        else :
            minGoodArr = min(minGoodArr, num);
        return True;
    nextStrArr = strArr + ["1"];
    if dfs(nextStrArr, n - 1) :
        return True
    nextStrArr = strArr + ["2"];
    if dfs(nextStrArr, n - 1) :
        return True
    nextStrArr = strArr + ["3"];
    if dfs(nextStrArr, n - 1) :
        return True

dfs([], n);
print(minGoodArr)