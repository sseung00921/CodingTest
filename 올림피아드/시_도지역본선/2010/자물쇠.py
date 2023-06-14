import sys;
input = sys.stdin.readline;
from collections import deque;

N = int(input());
Start = [i for i in range(1, N + 1)];
Locked = list(map(int, input().split()));
TmpLocked = Locked + [];

def checkIfReversed(i) :
    if i == N - 1 :
        if Locked[i] == 1 :
            return Locked[0] == N;
        else :
            return Locked[0] == Locked[i] - 1;
    else :
        if Locked[i] == 1 :
            return Locked[i + 1] == N;
        else :
            return Locked[i + 1] == Locked[i] - 1;

Locked = deque(Locked);
RversedInfos = [];
for i in range(1, N) :
    Locked.appendleft(Locked.pop());
    tmp = [];
    for j in range(0, N) :
        if checkIfReversed(j) :
            tmp.append(j);
            if j == N - 1 :
                RversedInfos.append((len(tmp), tmp, i));
        if len(tmp) > 0 and not checkIfReversed(j) :
            tmp.append(j);
            RversedInfos.append((len(tmp), tmp, i));
            tmp = []
Locked.appendleft(Locked.pop());
RversedInfos.sort(key = lambda x : -x[0]);

startK = RversedInfos[0][2];
Twitched = [RversedInfos[0][1][0] + 1, RversedInfos[0][1][-1] + 1];

for _ in range(startK) :
    Locked.appendleft(Locked.pop());

TwitchedStartIdx = RversedInfos[0][1][0];
TwitchedEndIdx = RversedInfos[0][1][-1];
arr = list(Locked);
part1 = arr[ : TwitchedStartIdx];
part2 = arr[TwitchedStartIdx : TwitchedEndIdx + 1];
part3 = arr[TwitchedEndIdx + 1 : ];
arr = part1 + part2[::-1] + part3;
Locked = deque(arr);

endK = -1;
for i in range(1, N) :
    Locked.appendleft(Locked.pop());
    if Locked[0] == 1 :
        endK = i;
        break;

if endK == -1 :
    Locked = TmpLocked + [];
    Locked = deque(Locked);
    for i in range(1, len(RversedInfos)) :
        if RversedInfos[i][2] != startK :
            startK = RversedInfos[i][2];
            Twitched = [RversedInfos[i][1][0] + 1, RversedInfos[i][1][-1] + 1];
            break;

    for _ in range(startK) :
        Locked.appendleft(Locked.pop());

    TwitchedStartIdx = Twitched[0] - 1;
    TwitchedEndIdx = Twitched[1] - 1;
    arr = list(Locked);
    part1 = arr[ : TwitchedStartIdx];
    part2 = arr[TwitchedStartIdx : TwitchedEndIdx + 1];
    part3 = arr[TwitchedEndIdx + 1 : ];
    arr = part1 + part2[::-1] + part3;
    Locked = deque(arr);

    endK = -1;
    for i in range(1, N) :
        Locked.appendleft(Locked.pop());
        if Locked[0] == 1 :
            endK = i;
            break;


print(endK);
print(*Twitched);
print(startK);