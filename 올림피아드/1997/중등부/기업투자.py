import sys;
input = sys.stdin.readline;

totalMoney, companyCnt = map(int, input().split());
investInfo = [];
d = [[[-1, None] for _ in range(companyCnt + 1)] for _ in range(totalMoney + 1)];
for _ in range(totalMoney) :
    data = list(map(int, input().split()));
    investInfo.append(data);
def dfs(remainMoney, companyNum) :
    if remainMoney == 0 or companyNum == companyCnt:
        return 0, [0] * (companyCnt - companyNum);

    if d[remainMoney][companyNum][0] != -1 :
        return d[remainMoney][companyNum][0], d[remainMoney][companyNum][1];

    maxGotProfit = 0;
    maxTrackingArr = None;
    gotProfit, gotTrackingArr = dfs(remainMoney, companyNum + 1);
    if gotProfit > maxGotProfit :
        maxGotProfit = gotProfit;
        maxTrackingArr = [0] + gotTrackingArr;
    for i in range(1, remainMoney + 1) :
        gotProfit = investInfo[i - 1][companyNum + 1] + dfs(remainMoney - i, companyNum + 1)[0];
        gotTrackingArr = [i] + dfs(remainMoney - i, companyNum + 1)[1]
        if gotProfit > maxGotProfit :
            maxGotProfit = gotProfit;
            maxTrackingArr = gotTrackingArr;
    d[remainMoney][companyNum] = maxGotProfit,maxTrackingArr
    return d[remainMoney][companyNum];

print(dfs(totalMoney, 0)[0]);
print(*dfs(totalMoney, 0)[1]);