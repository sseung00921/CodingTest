import sys;

input = sys.stdin.readline;
N = int(input());
Arr = list(map(int, input().split()));
Summ = sum(Arr);
FromLeftToRightByOneBee = Summ - Arr[0];
FromRightToLeftByOneBee = Summ - Arr[-1];

CumFromLeftToRight = [0] * len(Arr);
CumFromRightToLeft = [0] * len(Arr);
CumFromLeftToRight[0] = Arr[0];
for i in range(1, len(Arr)) :
    CumFromLeftToRight[i] = CumFromLeftToRight[i - 1] + Arr[i];
CumFromRightToLeft[len(Arr) - 1] = Arr[len(Arr) - 1];
for i in range(len(Arr) - 2, -1, -1) :
    CumFromRightToLeft[i] = CumFromRightToLeft[i + 1] + Arr[i];

Answer = -1;
#Left -> Right
for i in range(1, len(Arr)) :
    if i == len(Arr) - 1 :
        Answer = max(Answer, FromLeftToRightByOneBee - Arr[i]);
    else :
        Answer = max(Answer, FromLeftToRightByOneBee - Arr[i] + CumFromRightToLeft[i + 1]);
#Right -> Left
for i in range(len(Arr) - 2, -1, -1) :
    if i == 0 :
        Answer = max(Answer, FromRightToLeftByOneBee - Arr[i]);
    else :
        Answer = max(Answer, FromRightToLeftByOneBee - Arr[i] + CumFromLeftToRight[i - 1]);

#Left To Middle & Right To Middle
for i in range(1, len(Arr) - 1) :
    Answer = max(Answer,
                 (CumFromLeftToRight[i - 1] - CumFromLeftToRight[0]) +
                 (CumFromRightToLeft[i + 1] - CumFromRightToLeft[len(Arr) - 1]) +
                 2*Arr[i]
                 )

print(Answer);