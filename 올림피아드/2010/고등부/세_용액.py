import sys;
input = sys.stdin.readline;

N = int(input());
data = list(map(int, input().split()));
data.sort();

minDiff = abs(data[0] + data[1] + data[N - 1]);
answer = (data[0], data[1], data[N - 1]);
for root in range(N) :
    left = root + 1; right = N - 1;
    while left < right :
        summ = data[root] + data[left] + data[right];
        if abs(summ) < minDiff :
            minDiff = abs(summ);
            answer = (data[root], data[left], data[right]);
        if summ == 0 :
            break;
        elif summ < 0 :
            left += 1;
        elif summ > 0 :
            right -= 1;

print(*answer);