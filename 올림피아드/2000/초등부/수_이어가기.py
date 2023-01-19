n = int(input());
answer = -1;
answerArr = None;
for i in range(n//2, n + 1) :
    arr = [n];
    arr.append(i);
    while True :
        numToAppend = arr[-2] - arr[-1];
        if numToAppend < 0 :
            break;
        arr.append(numToAppend);
    if len(arr) > answer :
        answer = len(arr);
        answerArr = arr[:];
print(answer)
print(*answerArr)