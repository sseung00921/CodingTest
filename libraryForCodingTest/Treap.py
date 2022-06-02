#왠지 모르겠는데 이거 kth랑 erase 함수가 잘 동작 안함. 아무튼 혹시 나중에 수정하거나 참고할 일이 있을 것 같아 남겨둠.

import random

class Node :
    def __init__(self, key, totalNodeCnt) :
        self.key = key;
        self.priority = random.randint(1, totalNodeCnt)
        self.size = 1;
        self.left = None;
        self.right = None;

    def setLeft(self, newLeftNode) :
        self.left = newLeftNode;
        self.calcSize();

    def setRight(self, newRightNode) :
        self.right = newRightNode;
        self.calcSize();

    def calcSize(self) :
        size = 1;
        if self.left != None :
            size += self.left.size;
        if self.right != None :
            size += self.right.size;

def split(root, key) :
    if root == None :
        return (None, None);
    if root.key < key :
        rs = split(root.right, key);
        root.setRight(rs[0]);
        return (root, rs[1]);
    ls = split(root.left, key);
    root.setLeft(ls[1]);
    return (ls[0], root);

def insert(root, addedNode) :
    if root == None :
        return addedNode;
    if root.priority < addedNode.priority :
        splitted = split(root, addedNode.key);
        addedNode.setLeft(splitted[0]);
        addedNode.setRight(splitted[1]);
        return addedNode;
    elif addedNode.key < root.key :
        root.setLeft(insert(root.left, addedNode));
    else :
        root.setRight(insert(root.right, addedNode));
    return root;

def merge(a, b) :
    if a == None : return b;
    if b == None : return a;
    if a.priority < b.priority :
        b.setLeft(merge(a, b.left));
        return b;
    a.setRight(merge(a.right, b));
    return a;

def erase(root, key) :
    if root == None :
        return root
    if root.key == key :
        ret = merge(root.left, root.right);
        del root;
        return ret;
    if key < root.key :
        root.setLeft(erase(root.left, key));
    else :
        root.setRight(erase(root.right, key));
    return root;

def kth(root, k) :
    leftSize = 0;
    if root.left != None :
        leftSize = root.left.size;
    if k <= leftSize :
        return kth(root.left, k);
    if k == leftSize + 1 :
        return root;
    return kth(root.right, k - leftSize - 1);

def countLessThan(root, key) :
    if root == None :
        return 0;
    if root.key >= key :
        return countLessThan(root.left, key);
    ls = root.left.size if root.left != None else 0;
    return ls + 1 + countLessThan(root.right, key);


def inOrderTraverse(root) :
    if root == None :
        return;
    inOrderTraverse(root.left);
    print(root.key, end = ' ');
    inOrderTraverse(root.right);

nodeArr = [Node(i + 1, 50000) for i in range(0, 5)];
root = nodeArr[0];
for i in range(len(nodeArr)) :
    if i == 0 :
        continue;
    root = insert(root, nodeArr[i]);
print(root.key);
erase(root, 3);
inOrderTraverse(root)
