import sys;

input = sys.stdin.readline;
T = int(input());
Strs = [];
for _ in range(2*T) :
    Strs.append(input().rstrip());

def calNum(s) :
    expoArr = [0] * 1500001;
    nowDepthNum = 0;
    for i in range(len(s)) :
        if s[i] == '(' :
            nowDepthNum += 1;
        elif s[i] == ')' :
            if s[i - 1] == '(' :
                expoArr[nowDepthNum - 1] += 1;
            nowDepthNum -= 1;

    return expoArr;

def tuneExpoArr(expoArr) :
    for i in range(len(expoArr) - 1) :
        next = expoArr[i] // 2;
        remain = expoArr[i] % 2;
        expoArr[i + 1] += next;
        expoArr[i] = remain;

for i in range(0, len(Strs), 2) :
    a = Strs[i];
    b = Strs[i + 1];
    expoArrA = calNum(a);
    expoArrB = calNum(b);
    tuneExpoArr(expoArrA);
    tuneExpoArr(expoArrB);
    expoArrA.reverse();
    expoArrB.reverse();
    if expoArrA > expoArrB :
        print('>');
    elif expoArrA < expoArrB :
        print('<');
    elif expoArrA == expoArrB :
        print('=');