# 1보다 작은 실수
import random
print(random.random())

#10보다 작은 실수

for i in range(5):                   
 b = int(random.random()*10)              # range를 쓰면 리스트를 만들어준다.
print(b)

# 0~10사이의 랜덤 정수 출력

c = int(random.random()*11)
print(c)

# 1~10 사이의 랜덤 정수 출력

d = int((random.random()*10)+1)
print(d)


#자연수를 입력받아 그 숫자보다 작은 최대의 8의 배수

num = 433567688
mok = (num-1)//8
print(mok*8)

# 1년은 몇초인지
DAY_PER_YEAR = 365
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_HOUR = 60
SECONDS_IN_YEAR =DAY_PER_YEAR*HOURS_PER_DAY*MINUTES_PER_HOUR*SECONDS_PER_HOUR
print(f'1년은{SECONDS_IN_YEAR:,}초입니다.')

# 랜덤 조 만들어보기
import random
member =[]
member.append("홍길동")
member.append("전우치")
member.append("임꺽정")
member.append("심봉사")
random.shuffle(member)
print(member)

# append 활용  ar 소속
ar =[30,40,50,]
ar.append(45) 
print(ar)

# Tuple 활용
튜플 = ("사과", "귤", "수박")       
for a in 튜플: 
    print(a)
   
# list 활용
리스트 =["사과", "귤", "수박"]
for a in 리스트:
    print(a)

# 반복문 사용
kor = [75,80,70]
for item in kor:             
 print(item) 

 # 예 : 10와 8중 큰수는 10, 작은수는 8 입니다
num1 = int(input('첫번째 숫자 입력:'))
num2 = int(input('두번째 숫자 입력:'))
max = max(num1 , num2)
min = min(num1,  num2)
print(f'{num1}와 {num2}중 큰수는 {max} 작은수는{min}')

# 숫자를 입력받아 양수 , 음수 , 0을 출력
num = 2
if num>0:
     print('양수')
elif num<0:
     print('음수')
else:  
      print('0')

# 점수를 입력받아 70~90점이면 "추천대상", 아니면
# "대상아님"이라고 출력
score = 80
if score > 70 and  score<=90:
     print('추천대상') 
else:
     print('대상아님')
     
# 주민번호를 입력받아 성별을 출력

jumin = '971012-1035112'
if jumin[7] in ('1','3','5'):
    print('남자')
elif jumin[7] in ('2','4','5'):
    print('여자')
else:
    print('잘못된 문자입니다')

