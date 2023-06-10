import sys;
input = sys.stdin.readline;

N = int(input());
data = [-1] + list(map(int, input().split()));

AnswerArr = [-1] * (N + 1);
Stack = [];
for i in range(1, len(data)) :
    if len(Stack) == 0 :
        Stack.append((i, data[i]));
        AnswerArr[i] = 0;
    elif len(Stack) > 0 :
        thisHeight = data[i];
        while True :
            prevNum, prevHeight = Stack[-1];
            if thisHeight > prevHeight :
                Stack.pop();
            elif thisHeight < prevHeight :
                Stack.append((i, data[i]));
                AnswerArr[i] = prevNum;
                break;
            if len(Stack) == 0 :
                Stack.append((i, thisHeight));
                AnswerArr[i] = 0;
                break;

print(*AnswerArr[1 : ]);
