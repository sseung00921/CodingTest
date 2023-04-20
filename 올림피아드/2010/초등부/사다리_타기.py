import sys;
input = sys.stdin.readline;

k = int(input());
n = int(input());
startStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[0 : k];
destStr = input().rstrip();
Board = [];
for _ in range(n) :
    Board.append(input().rstrip());

def moveOneLevel(beforeStr, huddle) :
    beforeStr = list(beforeStr);
    for i in range(len(huddle)) :
        if huddle[i] == '-' :
            beforeStr[i], beforeStr[i + 1] = beforeStr[i + 1], beforeStr[i];
    return beforeStr;

def drawAnswer(beforeStr, afterStr) :
    rtnVal = ''
    for i in range(len(beforeStr) - 1) :
        if i > 0 and rtnVal[i - 1] == '-' :
            rtnVal += '*';
            continue;
        if beforeStr[i] == afterStr[i] :
            rtnVal += '*';
        elif beforeStr[i] == afterStr[i + 1] and beforeStr[i + 1] == afterStr[i] :
            rtnVal += '-';
        else :
            return 'x' * (k - 1);
    return rtnVal;

rightBeforeStr = startStr;
for i in range(n) :
    if Board[i][0] == '?' :
        break;
    rightBeforeStr = moveOneLevel(rightBeforeStr, Board[i]);

rightAfterStr = destStr;
for i in range(n - 1, -1, -1) :
    if Board[i][0] == '?':
        break;
    rightAfterStr = moveOneLevel(rightAfterStr, Board[i]);

answer = drawAnswer(rightBeforeStr, rightAfterStr);
print(answer);