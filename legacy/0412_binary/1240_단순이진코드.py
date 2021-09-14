#1240_단순 2진 암호코드
code = {(3,2,1,1):0,
        (2,2,2,1):1,
        (2,1,2,2):2,
        (1,4,1,1):3,
        (1,1,3,2):4,
        (1,2,3,1):5,
        (1,1,1,4):6,
        (1,3,1,2):7,
        (1,2,1,3):8,
        (3,1,1,2):9,}

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    data = [input() for _ in range(N)]
    #1. data안에서 암호코드 시작점 찾고
    #2.끝에서 부터확인(확실히 구분할 수 있어서), 7개 비트 확인
    #  7개 비트 확인하면, 0과 1의 구성모양을 확인하고 숫자 확인
    #3. 암호코드가 8자리니까 '2'를 8번 반복
    #4. 숫자 8개를 뽑아내면, 적절한 암호코드인지 확인하고 결과 출력
    #    적절한 암호가 아니면 0 출력 암호라면, 모든 코드 합 출력
    def solve():
        #data 안에서 암호코드 찾기
        for i in range(N):
            for j in range(M-1,-1,-1):      #뒤쪽 부터 검사
                    #1을 만나게 되면, 암호코드 시작
                if data[i][j] == "1":
                            # 여기서부터 암호 8자리 읽어오기
                    idx = j
                    pwd = list()
                    for k in range(8):
                        #각 암호코드가 어떻게 구성되어 있는지 확인:0과 1의 개수를 세겠다.
                        #각 0과 1이 몇개로 이루어져있는지 저장할 변수
                        n1 = n2 = n3 = n4 = 0
                        #뒤쪽 부터 세고 있기 때문에 n4부터 채워봅시다.
                        while data[i][idx] == "1":
                            n4 += 1  # 마지막 1의 개수
                            idx -= 1
                        while data[i][idx] == "0":
                            n3 += 1  # 마지막 1의 개수
                            idx -= 1
                        while data[i][idx] == "1":
                            n2 += 1  # 마지막 1의 개수
                            idx -= 1
                        n1 = 7 - n2 - n3 - n4   #암호코드 7개 에서 나머지 길이가 첫번째 0의 길이
                        idx -= n1       #다음 암호코드 시작점으로 인덱스 설정

                        pwd.insert(0,code[(n1,n2,n3,n4)])
                    #암호코드가 유효한 암호코드인지 확인하면 됩니다.
                    # “(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수가 되어야 한다.
                    # 0,2,4,6               1,3,5            7
                    odd_sum = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                    even_sum = pwd[1] + pwd[3] + pwd[5]
                    tmp = odd_sum*3 + even_sum + pwd[7]
                    if tmp % 10== 0:
                        # 올바른 암호코드
                        return odd_sum+ even_sum + pwd[7]
                    else:
                        #틀린 암호코드
                        return 0
    result = solve()
    print("#{} {}".format(tc, result))

