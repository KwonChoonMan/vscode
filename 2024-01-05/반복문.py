# 10 in list1 : 결과가 참 거짓 ( 10이 list1에 있니?)
# list1의 원소를 하나씩 꺼내 item에 담는 반복문
"""
list1 = [1,3,5]
for item in list1:
 print(item)

index=0
while index<3:
 print(list[index])
 index+=1

"""


"""
False는 무한반복을 할수가 없다.

1. 값추가 - > input('숫자 입력:')
2. 리스트 출력
   999. 종료: 감사합니다 - > 종료

"""
리스트 = []                         #  <----- 저장할곳
while True:
    print("1.값추가")
    print("2. 리스트 출력")
    print("3. 합계 출력")
    print("4. 평균 출력")
    print("999. 종료")
    
    select = input("번호 선택:")
    if select=='1':
        num = int(input('숫자 입력 :'))
        리스트.append(num)
    elif select=='2':
        print(리스트)
    elif select == '3' :
        print(f'입력값의 합계:{sum(리스트)}')
    elif select == '4':
        print(f'리스트의 평균:{sum(리스트)/len(리스트)}')
    elif select == '999':
        print("감사합니다")
        break
    else:
        print('메뉴를 정확하게 입력하세요')
    


