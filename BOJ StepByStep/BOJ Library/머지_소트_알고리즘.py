"""머지 소트 알고리즘이다. 여기서는 swap_count를 구해보는 약간의 부가 기능도 담겨 있다. 머지 소트 == O(logN) 버전의 버블 소트 라고 이해해도 무방하다."""
import sys;
input = sys.stdin.readline;

n = int(input());
data = list(map(int, input().split()));

def merge_sort(start, end) :
    global cnt;

    if start >= end :
        return;

    mid = (start + end) // 2;
    merge_sort(start, mid);
    merge_sort(mid + 1, end);

    temp = [];
    a = start;
    b = mid + 1;
    while a <= mid and b <= end :
        if data[a] <= data[b] :
            temp.append(data[a]);
            a += 1;
        else :
            temp.append(data[b]);
            b += 1;
            cnt += (mid - a + 1);
    if a <= mid :
        temp += data[a : mid + 1];
    if b <= end :
        temp += data[b : end + 1];

    for i in range(len(temp)) :
        data[start + i] = temp[i];

cnt = 0;
merge_sort(0, n - 1);
print(cnt);