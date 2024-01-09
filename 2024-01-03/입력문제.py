#  집의 가로와 세로를 입력받아 너비를 평으로 출력하시오
#  3.3 제곱미터가 1평
"""
width = int(input('가로길이입력:'))
length =int(input('세로길이입력:'))
너비 = width * length
평 = 너비/3.3
print(평)

"""
# 월급을 입력받아 연봉을 출력하시오
"""
may_pay = int(input('월급을 입력 :'))
one_year = may_pay * 12
print(one_year)

"""
# 월급을 입력받아 1년치소득세와 소득세를 제외한
# 연봉 실수령액(3481.2) 출력
# 소득세율은 3.3%
# income tax (소득세), actual receipt(실수령액)
"""
may_pay = int(input('월급을 입력:'))
one_year = may_pay * 12 
income_tax = one_year * 0.033
actual_receipt = one_year - income_tax
print(f'소득세:{income_tax}, 실수령액{actual_receipt}')

"""
# literal
"""
TAX_RATE = 0.033
my_pay = int(input('월급 입력 :'))
one_year = my_pay * 12
income_tax = one_year * TAX_RATE
actual_receipt = one_year - income_tax
print(f'소득세:{income_tax}, 실수령액{actual_receipt}')

"""
# 숫자를 입력받아 3의 배수인지 아닌지 출력하시오
"""
number = int(input('숫자 입력 :'))
if number%3==0:
   print('3의배수')
else:
   print("3의배수가아닙니다")
   """




# 점수를 입력 받아 90점이상이면 우수, 70점이상이면 패스, 미만
# 이면 낙제라고 출력하시오 (elif)
"""
jumsu = 90
jumsu = int(input('점수 입력:'))
if jumsu >=90:
    print('우수')
elif jumsu >= 70: 
    print('패스입니다')
else:
    print('낙제')
    """

# 국어, 영어 모두 70점 이상이면 합격 , 아니면 불합격
"""
kor,eng = 75,60
if kor>=70 and eng>=70:
    print('합격')
else:
    print('불합격')

"""
 # 숫자를 입력받아 음수면 양수로, 음수면 양수로 바꿔 출력
"""
num = int(input('숫자를 입력:'))
if num<0:
    print(-num)
else:
    print(-num)
"""

# 길이를 입력받아 센터미터면 인치로, 인치면 센티미터로 변경
# 1인치 = 2.54센티미터
"""
길이 = int(input('길이 입력:'))
센터미터 = int(input('센터미터 or 인치로 입력: '))
INCHI = 2.54
if 센터미터 == 'INCHI':
     print(길이*2.54, 'cm')
elif 센터미터=='cm':
    print(길이/2.54,'INCHI')
else: 
    print('cm 또는 INCHI를 입력하세요')
"""
# 임외로 가정
# 남자의 적정체중은 키-100, 여자의 적정체중은 키-105
# 키를 입력받아 적정체중을 출력하시오
"""
키 = int(input('키를 입력 : '))
성별 = input('성별을 입력(남자/여자)')
if 성별=='남자':
    print(키-100)
elif 성별 == '여자':
     print(키-105)
else:
     print('남자 또는 여자를 입력하세요')
"""



