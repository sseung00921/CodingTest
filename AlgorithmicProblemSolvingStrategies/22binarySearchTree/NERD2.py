import bisect;

N = 0;
SUM = 0;

def isDominatedByOther(personArr, p, q) :
    idx = bisect.bisect_left(personArr, (p, q));
    if idx == len(personArr) - 1 :
        return False;
    return personArr[idx][1] < personArr[idx + 1][1]

def removeDominatedByThis(personArr, p, q) :
    idx = bisect.bisect_left(personArr, (p, q));
    while True :
        if idx <= 0 or personArr[idx - 1][1] > personArr[idx][1] :
            break;
        personArr.pop(idx - 1);
        idx -= 1;

tc = int(input());
while tc > 0 :
    SUM = 0;
    N = int(input());
    personArr = [];
    for _ in range(N) :
        p, q = map(int, input().split());
        bisect.insort(personArr,(p, q));
        if isDominatedByOther(personArr, p, q) == True :
            personArr.remove((p, q));
            SUM += len(personArr);
            break;
        else :
            removeDominatedByThis(personArr, p, q);
            SUM += len(personArr);
    print(SUM);
    tc -= 1;