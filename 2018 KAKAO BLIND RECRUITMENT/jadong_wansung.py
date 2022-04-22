import copy;

def makeTree(words) :
    root = {};
    for word in words :
        cur_node = root;
        for c in word :
            cur_node.setdefault(c, [0, {}]);
            cur_node[c][0] += 1;
            cur_node = cur_node[c][1];
    return root;

def solution(words):
    learnedTree = makeTree(words);
    answer = 0
    for word in words :
        searchTree = learnedTree
        for c in word :
            answer += 1;
            if searchTree[c][0] == 1 :
                break;
            else :
                searchTree = searchTree[c][1];
    return answer

words = ["word","war","warrior","world"];
print(solution(words));