EmoCnt = 0;
Users = None;
Emoticons = None;
PossibleArr = [];

def calUserChoice(discountedPriceArr) :
    rtnArr = [0, 0];
    for user in Users :
        wannaPercent, assignCriAmount = user;
        thisUserTotal = 0;
        isAssigned = False;
        for emoInfo in discountedPriceArr :
            discountedPrice, discountPercent = emoInfo;
            if discountPercent >= wannaPercent :
                thisUserTotal += discountedPrice;
            if thisUserTotal >= assignCriAmount :
                rtnArr[0] += 1;
                isAssigned = True;
                break;
        if not isAssigned :
            rtnArr[1] += int(thisUserTotal);

    return rtnArr;


def dfs(emoIdx, discountedPriceArr) :
    if emoIdx == EmoCnt :
        PossibleArr.append(calUserChoice(discountedPriceArr));
        return;

    rawPrice = Emoticons[emoIdx];
    dfs(emoIdx + 1, discountedPriceArr + [(rawPrice*0.6, 40)]);
    dfs(emoIdx + 1, discountedPriceArr + [(rawPrice*0.7, 30)]);
    dfs(emoIdx + 1, discountedPriceArr + [(rawPrice*0.8, 20)]);
    dfs(emoIdx + 1, discountedPriceArr + [(rawPrice*0.9, 10)]);

    return;

def solution(users, emoticons):
    global EmoCnt;
    global Users;
    global Emoticons;
    EmoCnt = len(emoticons);
    Users = users;
    Emoticons = emoticons;

    dfs(0, []);
    PossibleArr.sort(key = lambda x : (-x[0], -x[1]));
    return PossibleArr[0];

users = [[40, 10000], [25, 10000]];
emoticons = [7000, 9000];
print(solution(users, emoticons));