#연습문제 2
#data = "01D06079861D79F99F"
data = "0F97A3"
#16진수 한자리 >>> 4개의 비트가 필요
#문자열 하나 읽어와서 4개 비트로 변환
#16진수 >>> 10진수로 변환
#c : 16진수를 나타내는 문자 하나
def hex_to_decimal(c):
    num = ord(c)
    #입력받은 문자가 숫자형태, 숫자로 만들기
    if ord('0') <= num <= ord('9'):
        return num - ord('0')
    else:   #A(10),B(11),C(12),D(13),E(14),F(15)
        return num - ord('A') + 10
#10진수 >> 2진수로 변환
#n : 0~15사이의  10진수 숫자 하나,
def decimal_to_binary(n):
    binary = [0] * 4        # 10진수 수를 이진수로 저장할 배열
    idx = 3
    #숫자 n를 2로 나누면서 나눈 나머지를 binary[idx]에 저장
    while n > 0:
        binary[idx] = n%2
        n //= 2
        idx -= 1
    return binary

print(ord('A'))
print(ord('8')-ord('0'))
# 0 : 48  1: 49 ......  9 : 57
#문자열 9를 이용해서 숫자9를 얻는 방법
#문자 9의 아스키코드 값에서, 문자0의 아스키 코드값을 빼면 됨
result = list()
for i in range(len(data)):
    decimal_num = hex_to_decimal(data[i])
    result += decimal_to_binary(decimal_num)

print(result)
