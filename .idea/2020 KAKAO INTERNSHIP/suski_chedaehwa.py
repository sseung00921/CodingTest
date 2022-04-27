from itertools import permutations;
import copy;

def calculateByOp(valFirst, valSecond, op) :
    if op == '*' :
        return int(valFirst)*int(valSecond);
    elif op == '+' :
        return int(valFirst) + int(valSecond);
    else :
        return int(valFirst) - int(valSecond);

def caculateFirst(arr, op) :
    stack = [];
    while len(arr) != 0 :
        tmp = arr.pop(0);
        if tmp == op :
            stack.append(calculateByOp(stack.pop(), arr.pop(0), op));
        else :
            stack.append(tmp);
    return stack;

def solution(expression):
    ops = ['*', '+', '-'];
    possibleOrders = list(permutations(ops, 3));

    arr = [];
    num = '';
    for c in expression :
        if c.isnumeric() :
            num += c;
        else :
            arr.append(int(num));
            arr.append(c);
            num = '';
    arr.append(num);

    answer = 0
    for possibleOrder in possibleOrders :
        tArr = copy.deepcopy(arr);
        for op in possibleOrder :
            tArr = caculateFirst(tArr, op)
        finalValue = abs(int(tArr.pop()));
        answer = max(answer, finalValue);
    return answer

expression = "100-200*300-500+20";
print(solution(expression));
