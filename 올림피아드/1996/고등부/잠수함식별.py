import sys;

input = sys.stdin.readline;

def dfs(s) :
    if len(s) == 0 :
        return True;
    if s[0] == '0' :
        if len(s) >= 2 and s[1] == '1' :
            return dfs(s[2 : ]);
        else :
            return False;
    elif s[0] == '1' :
        if len(s) >= 3 and s[1] == '0' and s[2] == '0' :
            for i in range(3, len(s)) :
                if s[i] == '1' :
                    if i == len(s) - 1 :
                        return dfs(s[i + 1 : ])
                    elif i != len(s) - 1 and s[i + 1] == '0' :
                        return dfs(s[i + 1 : ]);
                    elif i != len(s) - 1 and s[i + 1] == '1' :
                        if dfs(s[i + 1 : ]) or dfs(s[i + 2 : ]) :
                            return True;
    return False
s = input().rstrip();
if dfs(s) == True :
    print("SUBMARINE");
else :
    print("NOISE");