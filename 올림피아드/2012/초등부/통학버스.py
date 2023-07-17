import sys;
input = sys.stdin.readline;
from collections import deque;

N, K, S = map(int, input().split());
InfoOfLeftFromSchool = [];
InfoOfRightFromSchool = [];
for _ in range(N) :
    pos, cnt = map(int, input().split());
    if pos == S :
        continue;
    elif pos > S :
        InfoOfRightFromSchool.append([pos - S, cnt]);
    elif pos < S :
        InfoOfLeftFromSchool.append([S - pos, cnt]);

InfoOfLeftFromSchool.sort(key = lambda x : -x[0]);
InfoOfRightFromSchool.sort(key = lambda x : -x[0]);
InfoOfLeftFromSchool = deque(InfoOfLeftFromSchool);
InfoOfRightFromSchool = deque(InfoOfRightFromSchool);

TotalMoveMeter = 0;
while InfoOfLeftFromSchool :
    k = K;
    while k > 0 and InfoOfLeftFromSchool:
        if InfoOfLeftFromSchool[0][1] > k :
            InfoOfLeftFromSchool[0][1] -= k;
            TotalMoveMeter += InfoOfLeftFromSchool[0][0];
            k = 0;
        else :
            k -= InfoOfLeftFromSchool[0][1];
            TotalMoveMeter += InfoOfLeftFromSchool[0][0];
            InfoOfLeftFromSchool.popleft();
            while k > 0 and InfoOfLeftFromSchool :
                if InfoOfLeftFromSchool[0][1] > k :
                    InfoOfLeftFromSchool[0][1] -= k;
                    k = 0;
                else :
                    k -= InfoOfLeftFromSchool[0][1];
                    InfoOfLeftFromSchool.popleft();
while InfoOfRightFromSchool :
    k = K;
    while k > 0 and InfoOfRightFromSchool :
        if InfoOfRightFromSchool[0][1] > k :
            InfoOfRightFromSchool[0][1] -= k;
            TotalMoveMeter += InfoOfRightFromSchool[0][0];
            k = 0;
        else :
            k -= InfoOfRightFromSchool[0][1];
            TotalMoveMeter += InfoOfRightFromSchool[0][0];
            InfoOfRightFromSchool.popleft();
            while k > 0 and InfoOfRightFromSchool:
                if InfoOfRightFromSchool[0][1] > k :
                    InfoOfRightFromSchool[0][1] -= k;
                    k = 0;
                else :
                    k -= InfoOfRightFromSchool[0][1];
                    InfoOfRightFromSchool.popleft();

print(TotalMoveMeter * 2);