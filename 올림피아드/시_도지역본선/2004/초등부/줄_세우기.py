import sys;
input = sys.stdin.readline;

n = int(input());
pickedNums = list(map(int, input().split()));

students = [i for i in range(1, n + 1)];

for i, e in enumerate(pickedNums) :
    toInsertIdx = i - e;
    students.remove(i + 1);
    students.insert(toInsertIdx, i + 1);

print(*students);