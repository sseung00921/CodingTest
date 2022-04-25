def solution(N, stages):
    answer = []
    d = [0] * (N + 2);
    for stage in stages :
        d[stage] += 1;

    for i in range(1, N + 1) :
        if sum(d[i : ]) == 0 :
            failRate = 0;
            answer.append((failRate, i));
            continue;
        failRate = d[i] / sum(d[i : ]);
        answer.append((failRate, i));

    answer.sort(key=lambda s: (-s[0], s[1]));
    nAnswer = [];
    for tuple in answer :
        stage = tuple[1];
        nAnswer.append(stage);

    return nAnswer;

N = 5;
stages = [2, 1, 2, 6, 2, 4, 3, 3];
print(solution(N, stages));
