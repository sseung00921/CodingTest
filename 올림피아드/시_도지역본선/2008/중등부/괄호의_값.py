import sys;

input = sys.stdin.readline;
S = input().rstrip();

def check() :
    tmpS = list(S)
    nowNum = 0;
    for i in range(0, len(tmpS)) :
        if tmpS[i] == '(' or tmpS[i] == '[' :
            nowNum += 1;
        elif tmpS[i] == ')' or tmpS[i] == ']' :
            nowNum -= 1;

        if nowNum < 0 :
            return False;

    if nowNum != 0 :
        return False;

    for i in range(len(tmpS) - 1, -1, -1) :
        if tmpS[i] == '(' :
            if tmpS[i + 1] != ')' :
                return False;
            else:
                tmpS.pop(i + 1);
                tmpS.pop(i)
        elif tmpS[i] == '[' :
            if tmpS[i + 1] != ']' :
                return False;
            else:
                tmpS.pop(i + 1);
                tmpS.pop(i)

    return True;

def calc() :
    rtnVal = 0;
    nowSmallNum = 0;
    nowBigNum = 0;
    for i in range(0, len(S)) :
        if i > 0 and (S[i - 1] == '(' or S[i - 1] == '[') and (S[i] == ')' or S[i] == ']') :
            rtnVal += (2**nowSmallNum*3**nowBigNum);
        if S[i] == '(' :
            nowSmallNum += 1;
        elif S[i] == '[' :
            nowBigNum += 1;
        elif S[i] == ')' :
            nowSmallNum -= 1;
        elif S[i] == ']' :
            nowBigNum -= 1;

    return rtnVal;

if not check() :
    print(0);
else :
    print(calc());
