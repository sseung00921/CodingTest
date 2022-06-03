adj = [[0, 1, 1],[1, 0, 0],[1, 0, 0]];
CIRCUIT = [];

def getEulerCircuit(here) :
    for there in range(3) :
        while adj[here][there] > 0 :
            adj[here][there] -= 1;
            getEulerCircuit(there);
    CIRCUIT.append(here);

getEulerCircuit(0);
print(CIRCUIT);