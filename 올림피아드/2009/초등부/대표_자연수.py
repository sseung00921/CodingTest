import sys;
input = sys.stdin.readline;

n = int(input());
nums = list(map(int, input().split()));

nums.sort();
medians = [];
if n % 2 == 1 :
    medians.append(nums[n // 2]);
    print(medians[0]);
elif n % 2 == 0 :
    medians.append(nums[n // 2 - 1]);
    medians.append(nums[n // 2]);

    minVariance = int(1e9);
    answer = 0;
    for median in medians :
        variance = 0;
        for i in range(len(nums)) :
            variance += abs(nums[i] - median);
        if variance < minVariance :
            minVariance = variance;
            answer = median;
    print(answer);