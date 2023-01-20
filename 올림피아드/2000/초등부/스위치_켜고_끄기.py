import sys;
input = sys.stdin.readline;

def toggle(num) :
    if num == 0 :
        return 1;
    elif num == 1 :
        return 0;

def findBlancedRange(middle) :
    rtnI = 0;
    for i in range(1, n) :
        if middle - i < 1 or middle + i > n :
            break;
        if State[middle - i] != State[middle + i] :
            break;
        else :
            rtnI = i;

    return rtnI

n = int(input());
State = list(map(int, input().split()));
State = [-1] + State;
students = [];
m = int(input());
for _ in range(m) :
    gender, taken = map(int, input().split());
    students.append((gender, taken));

for i in range(m) :
    gender, taken = students[i];
    if gender == 1 :
        for j in range(taken, n + 1, taken) :
            State[j] = toggle(State[j]);
    else :
        k = findBlancedRange(taken);
        for j in range(taken - k, taken + k + 1) :
            State[j] = toggle(State[j]);

State = State[1 : ];
for i in range(0, n, 20) :
    print(*State[i : i + 20]);