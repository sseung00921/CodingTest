def solution(n, k, cmd):
    cursor = k;
    stack = [];
    answer = ["O"] * n;
    linkedList = {i : [i - 1, i + 1] for i in range(n)};
    linkedList[0][0] = None;
    linkedList[n - 1][1] = None;
    for c in cmd :
        if c == "C" :
            answer[cursor] = "X";
            prev = linkedList[cursor][0];
            next = linkedList[cursor][1];
            stack.append((prev, cursor, next));
            if next == None :
                cursor = linkedList[cursor][0];
            else :
                cursor = linkedList[cursor][1];
            if prev == None :
                linkedList[next][0] = None;
            elif next == None :
                linkedList[prev][1] = None;
            else :
                linkedList[next][0] = prev;
                linkedList[prev][1] = next;
        elif c == "Z" :
            prev, restoredIdx, next = stack.pop();
            answer[restoredIdx] = "O";
            if prev == None :
                linkedList[next][0] = restoredIdx;
            elif next == None :
                linkedList[prev][1] = restoredIdx;
            else :
                linkedList[next][0] = restoredIdx;
                linkedList[prev][1] = restoredIdx;
        elif c[0] == "U" or c[0] == "D":
            upDown, num = c.split(' ');
            num = int(num);
            if upDown == "U" :
                for i in range(num) :
                    prev = linkedList[cursor][0]
                    cursor = prev;
            elif upDown == "D" :
                for i in range(num) :
                    next = linkedList[cursor][1];
                    cursor = next;
    return ''.join(answer);

n = 8;
k = 2;
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"];
print(solution(n, k, cmd));