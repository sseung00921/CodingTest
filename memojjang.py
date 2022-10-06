import sys;
input = sys.stdin.readline;
n = int(input());
data = list(map(int, input().split()));

data.sort();

Minn = int(1e9*3);
answer = [];

i = 0;
j = n - 1;
while i < j :
    summ = data[i] + data[j];
    if abs(summ) < Minn :
        Minn = abs(summ);
        answer = [data[i], data[j]];
        if summ == 0 :
            break;
    if summ < 0 :
        i += 1;
    elif summ > 0 :
        j -= 1;

print(*answer);
