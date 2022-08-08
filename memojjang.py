mapper = {};

n = int(input());
data = list(map(int, input().split()));

m = int(input());
toCheckList = list(map(int, input().split()));

for num in data :
    if num in mapper :
        mapper[num] += 1;
    else :
        mapper[num] = 1;

answerArr = [];
for toCheck in toCheckList :
    if toCheck in mapper :
        answerArr.append(mapper[toCheck]);
    else :
        answerArr.append(0);

print(*answerArr);
