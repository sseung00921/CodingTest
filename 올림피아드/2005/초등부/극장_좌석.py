import sys;
input = sys.stdin.readline;

n = int(input());
m = int(input());
fixedArr = [0];
for _ in range(m) :
    fixedArr.append(int(input()));
fixedArr.append(n + 1);

d = [0] * 41;
d[1] = 1;
d[2] = 2;
for i in range(3, 41) :
    d[i] = d[i - 1] + d[i - 2];

spaceArr = [];
for i in range(1, len(fixedArr)) :
    spaceArr.append(fixedArr[i] - fixedArr[i - 1] - 1);

answer = 1;
for space in spaceArr :
    if space == 0 :
        continue;
    answer *= d[space];

print(answer);