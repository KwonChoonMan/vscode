lang = 'python'
# slicing
print(lang[0])      #p
print(lang[5])      #n
print('a' in lang) 
print('p'in lang)
# 리스트랑 튜플은 슬라이싱을 할수있다  
# 뒤에서 slicing   # 뒤에서 셀때는 0을 쓸수가 없기 때문에 -1 부터 시작한다.
print(lang[-1])

string = '123456789'
# 문자열[시작위치: 끝위치+1]
print(string[1:3])

# 문자열[시작위치:끝위치+1:간격]
print(string[1::5])

# 짝수만 출력  gender 자르다
print(string[1::2])

jumin = '961011-1021023'
gender = jumin[7]

# 남자인지 여자인지
if gender == '1':
    print('남자')
else:
     print('여자')

# 둘중의 하나 if문을 한줄로 - > 삼항연산자  ("남자" if gender=='1' else "여자")   - > 값이 오고 if가 오고 
# 복잡한 조건 삼항연산은 쓰지말자 --> 스파게티 코드
print("남자" if gender=='1' else "여자")   

# gender 가 1또는 3또는 5면 남자 아니면 여자

print("남자"if gender=='1'or'3'or'5' else "여자" )
print("남자"if gender in ('1','2','3') else "여자")

# 주민번호로 나이 출력하기
# 1. 올해의 년도
# 2. 태어난 년도 
# 3. 주민번호 앞 2자리를 슬라이싱한다 - > year
# 4. 주빈번호 7번쨰가 '1','2' - >  '19'를 + year
# 5. 주민번호 7번쨰가 '3' , '4' - > '20' + year
# 6. 올해의 년도 - int(태어난년도)
import datetime
this_year = datetime.datetime.now().year
year = jumin[0:2]
if jumin[7] in ('1','2'):
      year = int('19'+ year)
elif jumin[7] in ('3','4'):
     year =int('20' + year)
print(f'{this_year-year}세')

