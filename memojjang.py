a = 7;
b = a;
b += 1;
print("a = " + str(a));
print("b = " + str(b));

a = [1, 2, 3, 4, 5];
b = a;
b.pop();
print("a = " + str(a));
print("b = " + str(b));

arr = [[1,2],[1,2],[1,2]];
a = arr[0];
b = a;
b = b[1];
print("a = " + str(a));
print("b = " + str(b));