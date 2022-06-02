tc = int(input());
while tc > 0 :
    n = int(input());
    moves = list(map(int, input().split()));

    valArr = []
    for i in range(n) :
        valArr.append(i + 1);

    answerArr = [None] * n;
    for i in range(n - 1, -1, -1) :
        largerThanThis = moves[i];
        answerArr[i] = valArr[i - largerThanThis];
        valArr.pop(i - largerThanThis);

    print(*answerArr)
    tc -= 1;