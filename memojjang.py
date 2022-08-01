from collections import deque;

n = int(input());
wannaBe = [];
for _ in range(n) :
    wannaBe.append(int(input()));

idx = 0;
stack = deque([]);
ops = [];
for i in range(1, n + 1) :
    stack.append(i);
    ops.append('+')
    while len(stack) > 0  and stack[-1] == wannaBe[idx] :
        stack.pop();
        ops.append("-");
        idx += 1;

if len(stack) == 0 :
    for op in ops :
        print(op);
else :
    print("NO");