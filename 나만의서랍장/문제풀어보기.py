# 초를 입력받아 몇분 몇초인지 출력
# 예) 210초라고 입력하면 3분 30초

# input_seconds = 210
# minutes = input_seconds
# sceond = int(input('초입력: '))
# minutes = sceond//60 
# seconds = input_seconds%60
# print(f'{minutes}분{seconds}초')

# 분과 초를 입력하면 초를 출력
# 5분 10초 -> 310초
# 코드에 값이 직접 나타나는 것 : literal

# minutes = 5
# input_seconds = 10
# 상수는 대문자로
# SECONDS_PER_MINUTE = 60
# result = minutes * SECONDS_PER_MINUTE + input_seconds
# print(result)

# 몇일인지 입력받아 몇 개월 며칠인지 출력
# 333일 -> 11개월 3일

# day = int(input(' 입력:'))
# DAYS_PER_MONTH = 30
# days = 333
# months = 333//DAYS_PER_MONTH
# days = days%30
# print(f'{months}개월{days}일')

# 섭씨를 입력받아 화씨로 출력하시오c

# c1 = int(input('섭씨온도입력:'))
# c1 = 100
# h1 = c1 * (9/5) +32
# print(f'섭씨{c1}도는 화씨 {h1}도')

# 온도와 종류를 입력 받으시오
# 예) 온도: 35
# 예) 종류: 섭씨
# 종류가 섭씨면 온도를 화씨로 변환, 아니면 섭씨로 변환

# 1. 섭씨면 화씨로 화씨면 섭씨로 변경하는 프로그램
# 2. 온도 입력 -> 입력 온도가 섭씨? 화씨?
# 3. 섭씨 또는 화씨를 입력받는다 → kind
# 4. kind 가 섭씨면 화씨로 변환

tmep = int(input("온도입력 : "))
kind = input('변환할온도 종류(섭씨 또는 화씨)입력:')
if kind== '섭씨':
    print()
else: 
    print()




    







