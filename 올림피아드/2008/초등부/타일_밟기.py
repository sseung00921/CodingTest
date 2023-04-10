import sys;
input = sys.stdin.readline;

n = int(input());
data = list(map(int, input().split()));
setData = set(data);

answer = 0;

for i in range(len(data) - 1) :
    for j in range(i + 1, len(data)) :
        leap = data[j] - data[i];
        value = data[i] + data[j]
        checkingValue = data[j] + leap;
        isMoreThanThree = False;
        while checkingValue in setData :
            isMoreThanThree = True;
            value += checkingValue;
            checkingValue += leap;
        if isMoreThanThree :
            answer = max(answer, value);

print(answer);