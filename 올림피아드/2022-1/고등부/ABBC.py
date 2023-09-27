import sys;
from collections import deque;

input = sys.stdin.readline;
S = input().rstrip();

BQueue = deque([]);
BDeletedCheckArr = [0] * 300001;
Answer = 0;
for i in range(0, len(S)) :
    if S[i] == 'B' :
        BQueue.append(i);
    elif S[i] == 'C' :
        if BQueue :
            idx = BQueue.popleft();
            BDeletedCheckArr[idx] = 1;
            Answer += 1;

ABeforeCnt = 0;
for i in range(0, len(S)) :
    if S[i] == 'A' :
        ABeforeCnt += 1;
    elif S[i] == 'B' and not BDeletedCheckArr[i] :
        if ABeforeCnt > 0 :
            Answer += 1;
            ABeforeCnt -= 1;

print(Answer);