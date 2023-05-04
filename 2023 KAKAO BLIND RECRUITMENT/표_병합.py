Arr = [""] * 2500;
Parents = [i for i in range(0,2500)];

def setChildrenParent(beforeParent, afterParent) :
    for i in range(0, 2500) :
        if find_parent(i) == beforeParent :
            Parents[i] = afterParent;

def setChildrenVal(parent) :
    for i in range(0, 2500) :
        if find_parent(i) == parent :
            Arr[i] = Arr[parent];

def find_parent(x):
    if Parents[x] != x:
        Parents[x] = find_parent(Parents[x])
    return Parents[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    setChildrenParent(b, a);
    setChildrenVal(a);

def numPosTranslater(num) :
    return num // 50 + 1, num % 50 + 1;

def posNumTranslator(r, c) :
    r = int(r);
    c = int(c);
    r -= 1;
    c -= 1;
    return r * 50 + c;

def updateCell(r, c, val) :
    num = posNumTranslator(r, c);
    parent = find_parent(num);
    Arr[parent] = val;
    setChildrenVal(parent);

def updateVal(val1, val2) :
    for i in range(0, 2500) :
        if Arr[i] == val1 :
            r, c = numPosTranslater(i);
            updateCell(r, c, val2);

def merge(r1, c1, r2, c2) :
    num1 = posNumTranslator(r1, c1);
    num2 = posNumTranslator(r2, c2);
    if num1 != num2 :
        parent1 = find_parent(num1);
        parent2 = find_parent(num2);
        if Arr[parent1] == "" and Arr[parent2] != "" :
            union_parent(num2, num1);
        else :
            union_parent(num1, num2);

def unMerge(r, c) :
    num = posNumTranslator(r, c);
    parent = find_parent(num);
    Parents[num] = num;
    for i in range(0, 2500) :
        if i == num :
            continue;
        if find_parent(i) == parent :
            Arr[i] = "";
            Parents[i] = i;

def customPrint(r, c) :
    num = posNumTranslator(r, c);
    if Arr[num] == "" :
        return "EMPTY";
    else :
        return Arr[num];

def solution(commands):
    answer = []
    for cmd in commands :
        cmdArr = cmd.split();
        if cmdArr[0] == "UPDATE" :
            if len(cmdArr) == 4 :
                updateCell(cmdArr[1], cmdArr[2], cmdArr[3]);
            elif len(cmdArr) == 3 :
                updateVal(cmdArr[1], cmdArr[2]);
        elif cmdArr[0] == "MERGE" :
            merge(cmdArr[1], cmdArr[2], cmdArr[3], cmdArr[4]);
        elif cmdArr[0] == "UNMERGE" :
            unMerge(cmdArr[1], cmdArr[2]);
        elif cmdArr[0] == "PRINT" :
            answer.append(customPrint(cmdArr[1], cmdArr[2]));
    return answer

commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"];
print(solution(commands));