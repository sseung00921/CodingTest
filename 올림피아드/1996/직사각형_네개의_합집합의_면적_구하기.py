sqare1 = list(map(int, input().split()));
sqare2 = list(map(int, input().split()));
sqare3 = list(map(int, input().split()));
sqare4 = list(map(int, input().split()));

minMaxArr = [[0] * 102 for _ in range(102)];
sX1, sY1, eX1, eY1 = sqare1;
sX2, sY2, eX2, eY2 = sqare2;
sX3, sY3, eX3, eY3 = sqare3;
sX4, sY4, eX4, eY4 = sqare4;
for i in range(sX1, eX1) :
    for j in range(sY1, eY1) :
        minMaxArr[i][j] = 1;
for i in range(sX2, eX2) :
    for j in range(sY2, eY2) :
        minMaxArr[i][j] = 1;
for i in range(sX3, eX3) :
    for j in range(sY3, eY3) :
        minMaxArr[i][j] = 1;
for i in range(sX4, eX4) :
    for j in range(sY4, eY4) :
        minMaxArr[i][j] = 1;

answer = 0;
for i in range(102) :
    for j in range(102) :
        if minMaxArr[i][j] == 0 :
            continue;
        else :
            answer += 1;
print(answer);