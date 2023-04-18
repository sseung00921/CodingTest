import sys;
input = sys.stdin.readline;

n = int(input());
data = list(map(int, input().split()));

data.sort();

left = 0; right = n - 1;
minDiff = abs(data[left] + data[right]);
answer = (data[left], data[right]);
while left < right :
    summ = data[left] + data[right];
    if abs(summ) < minDiff :
        minDiff = abs(summ);
        answer = (data[left], data[right]);
    if summ == 0 :
        break;
    elif summ < 0 :
        left += 1;
    elif summ > 0 :
        right -= 1;

print(*answer);