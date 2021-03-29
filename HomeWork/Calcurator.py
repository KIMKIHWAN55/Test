n1 = int(input("첫번째 숫자를 입력:"))
n2 = int(input("두번째 숫자를 입력:"))
select = int(input("덧셈:1 뺄셈:2 곱셈:3 나눗셈:4")) # 더하기 뺄셈 곱셈 나눗셈중 무엇을할건지 선택
def  adder(n1,n2):   # 더하기값 두 함수를 더한다
     result = 0
     result = n1 + n2
     print("result=%d" %result)

def  minus(n1,n2):  #마이너스값 두 함수를 뺀다.
     result = 0
     result = n1 - n2
     print("result=%d" %result)

def  multi(n1,n2):   #곱하기값 두 함수를 곱한다.
     result = 0
     result = n1 * n2
     print("result=%d" %result)

def  div(n1,n2):# 나누기값 두 함수를 나눈다 .
     result = 0
     result = n1 / n2
     print("result=%d" %result)

if select == 1:#더하기 빼기 곱하기 나누기 할때 if문
    adder(n1,n2)
elif select == 2:
     minus(n1,n2)
elif select == 3:
     multi(n1,n2)
elif select == 4:
     div(n1,n2)







