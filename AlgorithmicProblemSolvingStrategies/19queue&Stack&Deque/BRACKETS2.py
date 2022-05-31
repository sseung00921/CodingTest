Opening = "({[";
Closing = ")}]";

def checkRight(s) :
    stack = [];
    for c in s :
        if c in Opening :
            stack.append(c);
        elif c in Closing :
            if len(stack) == 0 :
                return False;
            else :
                if Opening.find(stack[-1]) != Closing.find(c) :
                    return False;
                else :
                    stack.pop();

    if len(stack) == 0 :
        return True;
    return False;

tc = int(input());
while tc > 0 :
    s = input();
    if checkRight(s) :
        print("YES");
    else :
        print("NO");
    tc -= 1;