# (모듈) module : vscode의 확장프로그램 비슷, 남의 코드를 가져와 기능 확장 < library(기능들) < framewor (기능+사용법)

import random
print(random.random())

"""
for i in range(5):                   
    b =int(random.random()*10)              # range를 쓰면 리스트를 만들어준다.
    print(b)
"""

""""
c = int(random.random()*11)
print(c)

# 1~10 사이의 랜덤 정수 출력

d = int((random.random()*10)+1)
print(d)
"""


# 1년은 몆초인지 출력
"""
DAY_PER_YEAR = 365
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_HOUR = 60
print(DAY_PER_YEAR*HOURS_PER_DAY*MINUTES_PER_HOUR*SECONDS_PER_HOUR)

"""

# 45분간 일하고 10분씩, 전체 근무시간 480분이면
# 휴식 시간의 합계는 얼마인가?
"""
time = 480//55 
휴식시간합계 = time*10
print(휴식시간합계)

"""

# 숫자를 입력받아 1의 자리까지 버리고 출력
# 예 ) 3512 - > 3510 , 359 - > 350
"""
num = 3512
result = num - num%10
print(result)
"""

# 자연수를 입력받아 그 숫자보다 작거나 같은 최대의 7의 배수
# 예) 17->14 ,21->21
# 0-6    0  7*0
# 7-13   7  7*1
# 14-20  14 7*2
num = 7
mok = (num)//7
print(mok*7)



# 자연수를 입력받아 그 숫자보다 작은 최대의 7의 배수
# 예 ) 17 - > 14 , 21 ->14
# 1-7    0   7*0
# 8 -14  //7  7*1
# 15-21  14  7*2
num = 17
mok = (num-1)//7
print(mok*7)



# 숫자를 입력받아 양수 , 음수 , 0을 출력

# num = 2
# if num>0:
#     print('양수')
# elif num<0:
#     print('음수')
# else:  
#      print('0')

# 점수를 입력받아 70~90점이면 "추천대상", 아니면
# "대상아님"이라고 출력

# score = None
# if score >= 70 and score<=90:
#     print('추천대상')
# else:
#     print('대상아님')
     

# 주민번호를 입력받아 성별을 출력
jumin = '971012-1035112'
if jumin[7] in ('1','3','5'):
    print('남자')
elif jumin[7] in ('2','4','5'):
    print('여자')
else:
    print('잘못된 문자입니다')







