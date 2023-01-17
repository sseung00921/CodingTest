import sys;
input = sys.stdin.readline;

n = int(input());
a, b = map(int, input().split());
m = int(input());
jokbo = dict();
Parents = [-1] * (n + 1);
for _ in range(m) :
    parent, child = map(int, input().split());
    if parent not in jokbo :
        jokbo[parent] = [child];
    else :
        jokbo[parent].append(child);
    Parents[child] = parent;

minDist = 250;
for i in range(1, 101) :
    parentA = a;
    distFromA = 0;
    while parentA != i :
        parentA = Parents[parentA];
        distFromA += 1;
        if parentA == -1 :
            distFromA = 1000;
            break;

    parentB = b;
    distFromB = 0;
    while parentB != i :
        parentB = Parents[parentB];
        distFromB += 1;
        if parentB == -1 :
            distFromB = 1000;
            break;

    minDist = min(minDist, distFromA + distFromB);

if minDist == 250 :
    minDist = -1;
print(minDist);

