import sys;
input = sys.stdin.readline;

data = [];
for _ in range(5) :
    data.append(int(input()));

print(int(sum(data) / 5));
data.sort();
print(data[2]);