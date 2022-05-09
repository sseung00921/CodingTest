#n진수 to 10진
print(int('101',2)); #두 번째 파라미터가 base n 앞의 파라미터가 변환할 n진수

#n진 to 2,8,16진수
print(bin(11)[2:])
print(oct(11)[2:])
print(hex(11)[2:])

#10진수 to n진수
def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

print(solution(45, 3))

#n진수 to n진수
print(solution(int('21',3),7)); #첫번째 파라미터에서 n진수를 10진수로 변환해서 위의 10 to n 진수 함수 적용

