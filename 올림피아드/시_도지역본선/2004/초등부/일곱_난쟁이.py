from itertools import combinations;

import sys;
input = sys.stdin.readline;

data = [];
for _ in range(9) :
    data.append(int(input()));

answer = None;
for selected in list(combinations(data, 7)) :
    if sum(selected) == 100 :
        answer = list(selected);
        break;

answer.sort();
for e in answer :
    print(e);