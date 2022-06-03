N = 0;
WORDS = None;
ADJ = None;
INDEGREE = None;
OUTDEGREE = None;
EDGES = None;
CIRCUIT = None;

def makeGraph(WORDS) :
    for word in WORDS :
        start = ord(word[0]) - ord('a');
        end = ord(word[-1]) - ord('a');
        EDGES[start][end].append(word);
        ADJ[start][end] += 1;
        OUTDEGREE[start] += 1;
        INDEGREE[end] += 1;

def checkCanBeOiler() :
    moreOutDegreeByOne = 0; moreInputDegreeByOne = 0;
    for i in range(26) :
        delta = INDEGREE[i] - OUTDEGREE[i];
        if delta < -1 or delta > 1 :
            return False;
        elif delta == 1 :
            moreInputDegreeByOne += 1;
        elif delta == -1 :
            moreOutDegreeByOne += 1;
    if (moreInputDegreeByOne == 1 and moreOutDegreeByOne == 1) or (moreInputDegreeByOne == 0 and moreOutDegreeByOne == 0) :
        return True;
    return False;

def findOilerCircuit(here) :
    for there in range(26) :
        while ADJ[here][there] > 0 :
            ADJ[here][there] -= 1;
            findOilerCircuit(there);
    CIRCUIT.append(here);

def findOilerCircuitOrTrail() :
    for i in range(26) :
        if OUTDEGREE[i] == INDEGREE[i] + 1 :
            findOilerCircuit(i);
            return;
    for i in range(26) :
        if OUTDEGREE[i] > 0 :
            findOilerCircuit(i);
            return;

tc = int(input());
while tc > 0 :
    ADJ = [[0] * 26 for _ in range(26)];
    INDEGREE = [0] * 26;
    OUTDEGREE = [0] * 26;
    EDGES = [[[] for _ in range(26)] for _ in range(26)];

    N = int(input());
    WORDS = [];
    for _ in range(N) :
        WORDS.append(input());

    makeGraph(WORDS);

    CIRCUIT = [];
    if checkCanBeOiler() == False :
        print("IMPOSSIBLE");
    else :
        findOilerCircuitOrTrail();
        CIRCUIT.reverse();
        if len(CIRCUIT) != N + 1 :
            print("IMPOSSIBLE");
        else :
            rtnStr = '';
            for i in range(1, len(CIRCUIT)) :
                if len(rtnStr) > 0 :
                    rtnStr += ' ';
                edge = EDGES[CIRCUIT[i - 1]][CIRCUIT[i]].pop();
                rtnStr += edge;
            print(rtnStr);
    tc -= 1;
