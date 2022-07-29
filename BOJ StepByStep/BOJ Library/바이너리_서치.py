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