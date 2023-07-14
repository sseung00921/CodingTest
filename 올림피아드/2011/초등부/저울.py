import sys;
input = sys.stdin.readline;

N = input();
data = list(map(int, input().split()));
data.sort();

target = 1;
for i in range(len(data)) :
    if target < data[i] :
        break;
    else :
        target += data[i];
print(target);