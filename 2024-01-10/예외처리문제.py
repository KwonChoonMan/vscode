# 정수변수를 2개 만들어, 나눗셈 결과를 출력하시오
# 예외처리가 필요하면 예외처리하시오
"""
try:
 x = 10
 y = 0 
 print(x/y)
except:
 print("0으로 나눌 수 없습니다")
 
"""
# 나눗셈 결과를 리턴하는 함수
"""
def divide(a:int,b:int):
    try:
        return a/b
    except:
        return None
"""