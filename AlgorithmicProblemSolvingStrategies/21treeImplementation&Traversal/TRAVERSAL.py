N = 0;

tc = int(input());

def makePostOrders(preOrders, inOrders) :
    if len(preOrders) == 0 :
        return;

    root  = preOrders[0];
    rootIdxInInOrders = inOrders.index(root);

    makePostOrders(preOrders[1 : rootIdxInInOrders + 1], inOrders[0 : rootIdxInInOrders]);
    makePostOrders(preOrders[rootIdxInInOrders + 1 : ], inOrders[rootIdxInInOrders + 1 : ]);
    print(root, end = ' ');
    return;

while tc > 0 :
    N = int(input());
    preOrders = list(map(int, input().split()));
    inOrders = list(map(int, input().split()));
    postOrders = makePostOrders(preOrders, inOrders);
    tc -= 1;
