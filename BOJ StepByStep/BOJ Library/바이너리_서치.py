n = int(input());
data = list(map(int, input().split()));
data.sort();
m = int(input());
toFindArr = list(map(int, input().split()));

def bSearch(left, right, target) :
    while left <= right :
        mid = (left + right) // 2
        if data[mid] == target :
            return 1;
        elif data[mid] < target:
            left = mid + 1
        elif data[mid] > target:
            right = mid - 1
    return 0;



for num in toFindArr :
    print(bSearch(0, n - 1, num));

#--- 나무 자르기 프로토타입

n, target = map(int, input().split());
trees = list(map(int, input().split()));

INF = int(1e9);
answer = -INF;

def bSearch(left, right, target) :
    global answer;
    while left <= right :
        mid = (left + right) // 2
        summ = 0;
        for tree in trees :
            if tree > mid :
                summ += (tree - mid);
        if summ < target:
            right = mid - 1
        elif summ >= target:
            answer = max(answer, mid);
            left = mid + 1
    return mid;

#첫번째 파라미터에는 자를 수 있는 범위의 최솟값이 두번째 파라미터에는 자를 수 있는 범위의 최댓값이 들어가야 한다. 특히 첫번째 파라미터에는 0이 들어갈 수 있는지 혹은 1부터 들어갈 수 있는지를 신경쓴다!!!
#특히 mid의 값으로 나눠야 하는 연산을 하게 될 때에는 첫번째 파라미터가 0이 아니라 1부터 시작하도록 신경쓴다.
bSearch(0, max(trees), target);
print(answer);