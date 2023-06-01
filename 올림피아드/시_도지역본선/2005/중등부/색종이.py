import sys;
input = sys.stdin.readline;
Answer = 0;

Inven = [0];
for _ in range(6) :
    Inven.append(int(input()));

while Inven[6] > 0 :
    Inven[6] -= 1;
    Answer += 1;

while Inven[5] > 0 :
    emptyCnt = 36;
    Inven[5] -= 1;
    emptyCnt -= 25;
    Inven[1] = max(Inven[1] - emptyCnt, 0);
    Answer += 1;

while Inven[4] > 0 :
    emptyCnt = 36;
    Inven[4] -= 1;
    emptyCnt -= 16;
    emptyCnt -= min(Inven[2], 5) * 4;
    Inven[2] = max(Inven[2] - min(Inven[2], 5), 0);
    Inven[1] = max(Inven[1] - emptyCnt, 0);
    Answer += 1;

while Inven[3] > 0 :
    emptyCnt = 36;
    if Inven[3] >= 4 :
        emptyCnt -= 36;
        Inven[3] -= 4;
    elif Inven[3] == 3 :
        Inven[3] -= 3;
        emptyCnt -= 27;
        emptyCnt -= min(Inven[2], 1) * 4
        Inven[2] = max(Inven[2] - min(Inven[2], 1), 0);
    elif Inven[3] == 2 :
        Inven[3] -= 2;
        emptyCnt -= 18;
        emptyCnt -= min(Inven[2], 3) * 4
        Inven[2] = max(Inven[2] - min(Inven[2], 3), 0);
    elif Inven[3] == 1 :
        Inven[3] -= 1;
        emptyCnt -= 9;
        emptyCnt -= min(Inven[2], 5) * 4
        Inven[2] = max(Inven[2] - min(Inven[2], 5), 0);
    Inven[1] = max(Inven[1] - emptyCnt, 0);
    Answer += 1;

while Inven[2] > 0 :
    emptyCnt = 36;
    emptyCnt -= min(Inven[2], 9) * 4;
    Inven[2] = max(Inven[2] - min(Inven[2], 9), 0);
    Inven[1] = max(Inven[1] - emptyCnt, 0);
    Answer += 1;

while Inven[1] > 0 :
    emptyCnt = 36;
    Inven[1] = max(Inven[1] - 36, 0);
    Answer += 1;

print(Answer);