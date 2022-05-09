import math;
sosuSet = set();

def solution(n): # 1 ~ n까지의 정수 중 모든 소수(prime number)를 찾아 set에 넣기
    arr = [True for _ in range(n + 1)];
    arr[0] = False; arr[1] = False;
    for i in range(2, int(math.sqrt(n)) + 1) :
        if arr[i] == True :
            j = 2
            while i*j <= n :
                arr[i*j] = False;
                j += 1;
    for i in range(2, n + 1) :
        if arr[i] == True :
            sosuSet.add(i);