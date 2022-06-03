import random;

class Node :
    def __init__(self, key):
        self.key = key;
        self.priority = random.randint(1, 50000);
        self.size = 1;
        self.left = None;
        self.right = None;

    def calcSize(self):
        self.size = 1;
        if self.left != None : self.size += self.left.size;
        if self.right != None : self.size += self.right.size;

    def setLeft(self, newLeft):
        self.left = newLeft;
        self.calcSize();

    def setRight(self, newRight):
        self.right = newRight;
        self.calcSize();

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

def insert(root, node) :
    if root == None :
        return node;
    if root.priority < node.priority :
        splitted = split(root, node.key);
        node.setLeft(splitted[0]);
        node.setRight(splitted[1]);
        return node;
    elif node.key < root.key :
        root.setLeft(insert(root.left, node));
    else :
        root.setRight(insert(root.right, node));
    return root;

def merge(a, b) :
    if a == None : return b;
    if b == None : return a;
    if a.priority < b.priority :
        if a.key < b.key :
            b.setLeft(merge(a, b.left));
            return b;
        else :
            b.setRight(merge(a, b.right));
            return b;
    else :
        if a.key < b.key :
            a.setRight(merge(a.right, b));
            return a;
        else :
            a.setLeft(merge(a.left, b));
            return a;

def erase(root, key) :
    if root == None : return root;
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
    if root.left != None : leftSize = root.left.size;
    if k <= leftSize : return kth(root.left, k);
    if k == leftSize + 1 : return root;
    return kth(root.right, k - leftSize - 1);

def countLessThan(root, key) : #이 함수가 곧 특정 키의 인덱스를 반환해주는 함수와 같다. 즉 위의 함수와 인풋 아웃풋이 반대인 함수이다.
    if root == None : return 0;
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

root = None;
root = insert(root, Node(5));
root = insert(root, Node(4));
root = insert(root, Node(3));
root = insert(root, Node(2));
root = insert(root, Node(1));
print(kth(root, 3).key);
print(countLessThan(root, 3) + 1);
root = erase(root, 3);
root = erase(root, 2);
root = erase(root, 2);
inOrderTraverse(root);
