N = 0;
Graph = None;
Order = None;
Visited = None;

def makeGraph(data) :
    for i in range(1, len(data)) :
        j = i - 1;
        length = min(len(data[j]), len(data[i]));
        for k in range(length) :
           if data[i][k] != data[j][k] :
               Graph[ord(data[j][k]) - ord('a')][ord(data[i][k]) - ord('a')] = 1;
               break;


def dfs(start) :
    Visited[start] = True;
    for i in range(26) :
        if Graph[start][i] == 1 and Visited[i] == False :
            dfs(i);
    Order.append(start);

tc = int(input());
while tc > 0 :
    Graph = [[0] * 26 for _ in range(26)];
    N = int(input());
    data = [];
    for _ in range(N) :
        data.append(input());
    makeGraph(data);
    Order = [];
    Visited = [False] * 26;
    for i in range(26) :
        if Visited[i] == False :
            dfs(i);
    Order.reverse()
    isCycle = False;
    for i in range(len(Order)) :
        for j in range(i + 1, len(Order)) :
            if Graph[Order[j]][Order[i]] == 1 :
                isCycle = True;
                break;
        if isCycle :
            break;
    if isCycle :
        print("INVALID HYPOTHESIS")
    else :
        answerArr = [];
        for i in Order :
            answerArr.append(chr(i + ord('a')));
        print("".join(answerArr));
    tc -= 1;