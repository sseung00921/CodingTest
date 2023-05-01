DeliveredLastPoint = -1;
PickUpedLastPoint = -1;
Cap = 0;
Deliveries = None;
PickUps = None;

def doDeliver() :
    global DeliveredLastPoint;
    remain = Cap;
    start = DeliveredLastPoint
    for i in range(start, -1, -1) :
        if Deliveries[i] > 0 :
            if remain >= Deliveries[i] :
                remain -= Deliveries[i];
                Deliveries[i] = 0;
                DeliveredLastPoint -= 1;
            elif remain < Deliveries[i] :
                Deliveries[i] -= remain;
                break;
        elif Deliveries[i] == 0 :
            DeliveredLastPoint -= 1;

    return;

def doPickUp() :
    global PickUpedLastPoint;
    remain = Cap;
    start = PickUpedLastPoint
    for i in range(start, -1, -1) :
        if PickUps[i] > 0 :
            if remain >= PickUps[i] :
                remain -= PickUps[i];
                PickUps[i] = 0;
                PickUpedLastPoint -= 1;
            elif remain < PickUps[i] :
                PickUps[i] -= remain;
                break;
        elif PickUps[i] == 0 :
            PickUpedLastPoint -= 1;

    return;

def solution(cap, n, deliveries, pickups):
    global DeliveredLastPoint;
    global PickUpedLastPoint;
    global Cap;
    global Deliveries;
    global PickUps;
    DeliveredLastPoint = -1;
    PickUpedLastPoint = -1;
    Cap = cap;
    Deliveries = deliveries;
    PickUps = pickups;
    for i in range(n - 1, -1, -1) :
        if Deliveries[i] > 0 :
            DeliveredLastPoint = i;
            break;
    for i in range(n - 1, -1, -1) :
        if PickUps[i] > 0 :
            PickUpedLastPoint = i;
            break;

    answer = 2 * (max(DeliveredLastPoint, PickUpedLastPoint) + 1);
    while DeliveredLastPoint != -1 or PickUpedLastPoint != -1 :
        doDeliver();
        doPickUp();
        answer += 2 * (max(DeliveredLastPoint, PickUpedLastPoint) + 1);
    return answer;

cap = 2;
n = 7;
deliveries = [1, 0, 2, 0, 1, 0, 2];
pickups = [0, 2, 0, 1, 0, 2, 0];
print(solution(cap, n, deliveries, pickups));