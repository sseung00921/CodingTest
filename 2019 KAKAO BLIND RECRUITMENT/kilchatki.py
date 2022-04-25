import sys;
sys.setrecursionlimit(10000000);

class Node :
    def __init__(self, i, x, y) :
        self.id = i;
        self.x = x;
        self.y = y;
        self.left = None;
        self.right = None;

    def __lt__(self, other) :
        return self.y > other.y;

def addNode(node, root) :
    if node.x < root.x :
        if root.left is None :
            root.left = node;
        else :
            addNode(node, root.left);
    else :
        if root.right is None :
            root.right = node;
        else :
            addNode(node, root.right);

def preOrderTraverse(preOrderList, root) :
    if root is None :
        return;
    preOrderList.append(root.id);
    preOrderTraverse(preOrderList, root.left);
    preOrderTraverse(preOrderList, root.right);

def postOrderTraverse(postOrderList, root) :
    if root is None :
        return;
    postOrderTraverse(postOrderList, root.left);
    postOrderTraverse(postOrderList, root.right);
    postOrderList.append(root.id);


def solution(nodeinfo):
    lenNodeinfo = len(nodeinfo);
    nodeList = [];

    for i in range(lenNodeinfo) :
        x, y = nodeinfo[i];
        nodeList.append(Node(i + 1, x, y));
    nodeList.sort();

    root = nodeList[0];
    for i in range(1, lenNodeinfo) :
        addNode(nodeList[i], root);

    answer = [];
    preOrderList = [];
    postOrderList = [];
    preOrderTraverse(preOrderList, root);
    postOrderTraverse(postOrderList, root);
    answer.append(preOrderList);
    answer.append(postOrderList);
    return answer;


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]];
print(solution(nodeinfo));