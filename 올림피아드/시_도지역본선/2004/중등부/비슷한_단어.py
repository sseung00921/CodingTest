import sys;
input = sys.stdin.readline;

n = int(input());
data = [];
for _ in range(n) :
    data.append(input().rstrip());

WordToCompare = data[0];
data = data[1 : ];

def checkIfSimillarConstitution(a, b) :
    aCntArr = [0] * 26;
    bCntArr = [0] * 26;

    for i in range(len(a)) :
        idx = ord(a[i]) - ord('A');
        aCntArr[idx] += 1;
    for i in range(len(b)) :
        idx = ord(b[i]) - ord('A');
        bCntArr[idx] += 1;

    return permitBoradlySame(aCntArr, bCntArr);

def permitBoradlySame(arr1, arr2) :
    if abs(sum(arr1) - sum(arr2)) == 1 :
        useChance = False;
        for i in range(len(arr1)) :
            if arr1[i] == arr2[i] :
                continue;
            else :
                if (not useChance) and abs(arr1[i] - arr2[i]) == 1:
                    useChance = True;
                    continue;
                else :
                    return False;
    elif sum(arr1) == sum(arr2) :
        diffCnt = 0;
        for i in range(len(arr1)) :
            if arr1[i] != arr2[i] :
                if abs(arr1[i] - arr2[i]) == 1 :
                    diffCnt += 1;
                    continue;
                else :
                    return False;
        if diffCnt == 0 or diffCnt == 2 :
            return True
        else :
            return False;
    else :
        return False;

    return True;

answer = 0;
for e in data :
    if checkIfSimillarConstitution(WordToCompare, e) :
        answer += 1;

print(answer);