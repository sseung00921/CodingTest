from itertools import combinations;
from bisect import bisect_left;
MaxWin = -1;
Answer = None;
R = 0;
ArstArr = [];
BrstArr = [];
Dice = None;
def dfs(level, whoArr, who, score) :
    global ArstArr; global BrstArr;
    if level == R :
        if who == 'a' :
            ArstArr.append(score);
            return;
        elif who == 'b' :
            BrstArr.append(score);
            return;
    for i in range(6) :
        dfs(level + 1, whoArr, who, score + Dice[whoArr[level] - 1][i]);

def cal(Alst, Blst) :
    global MaxWin;
    global Answer;
    dfs(0, Alst, 'a', 0);
    dfs(0, Blst, 'b', 0);
    BrstArr.sort();
    winCnt = 0;
    for e in ArstArr :
        winCnt += bisect_left(BrstArr, e);
    if winCnt > MaxWin :
        MaxWin = winCnt;
        Answer = Alst;


def solution(dice):
    global R;
    global ArstArr; global BrstArr;
    global Dice;
    Dice = dice;
    r = len(dice) // 2;
    R = r;
    all = [i for i in range(1, len(dice) + 1)];
    for lst in combinations(all, r) :
        AChoose = lst;
        tmp = [];
        for i in range(1, len(dice) + 1) :
            if i not in AChoose :
                tmp.append(i);
        BChoose = tmp;
        ArstArr = []; BrstArr = [];
        cal(AChoose, BChoose);
    return Answer;

dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]];
print(solution(dice));