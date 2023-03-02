import sys;
input = sys.stdin.readline;
from itertools import combinations;

n = int(input());
data = [];
for _ in range(n) :
    data.append(list(map(int, input().split())));

def findBestNum(givenFive) :
    bestNum = -1;
    for partArr in combinations(givenFive, 3) :
        summ = sum(partArr);
        summ %= 10;
        bestNum = max(bestNum, summ);
    return bestNum;

bestNumForEachMemberArr = [];
for i in range(len(data)) :
    bestNumForEachMemberArr.append((i + 1, findBestNum(data[i])));

bestNumForEachMemberArr.sort(key = lambda x : (-x[1], -x[0]));
print(bestNumForEachMemberArr[0][0]);