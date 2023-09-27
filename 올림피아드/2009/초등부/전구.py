import sys;
from bisect import bisect_left;
from collections import deque;

input = sys.stdin.readline;
N = int(input());
Switches = [0] + list(map(int, input().split()));
Bulbes = [0] + list(map(int, input().split()));
SwitchOrders = dict();
RSwitchOrders = dict();
for i in range(1, N + 1) :
    SwitchOrders[Switches[i]] = i;
    RSwitchOrders[i] = Switches[i];
for i in range(1, N + 1) :
    Bulbes[i] = SwitchOrders[Bulbes[i]];

Stack = [Bulbes[1]];
Before = [-1] * (N + 1);
LenArr = [-1] * (N + 1);
LenArr[Bulbes[1]] = 1;
for i in range(2, N + 1) :
    if Bulbes[i] > Stack[-1] :
        Before[Bulbes[i]] = Stack[-1];
        Stack.append(Bulbes[i]);
        LenArr[Bulbes[i]] = len(Stack);
    else :
        idx = bisect_left(Stack, Bulbes[i]);
        if idx == 0 :
            Before[Bulbes[i]] = -1;
        else :
            Before[Bulbes[i]] = Stack[idx - 1];
        Stack[idx] = Bulbes[i];
        LenArr[Bulbes[i]] = idx + 1;

MaxLen = -1;
StartBulbNum = -1;
for i in range(1, N + 1) :
    if LenArr[i] > MaxLen :
        MaxLen = LenArr[i];
        StartBulbNum = i;

AnswerStack = deque([StartBulbNum]);
while Before[StartBulbNum] != -1 :
    AnswerStack.appendleft(Before[StartBulbNum]);
    StartBulbNum = Before[StartBulbNum];

AnswerStack = [RSwitchOrders[e] for e in AnswerStack];
AnswerStack.sort();
print(len(AnswerStack));
print(*AnswerStack)

