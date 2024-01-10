# 할일 관리
todos=[
    {'tno':1, 'title':'할일','reg_day':'2024-01-09','finish':False},
    {'tno':3, 'title':'할일3','reg_day':'2024-01-09','finish':False}
]
tno=2
#CRUD
# Read : 전체읽기 , 1개읽기
for todo in todos:
  print(todo)
  # 할일 번호를 입력받아 찾아서 출력
  input_tno = int(input('할일번호입력:'))
  찾았니 = False
  for todo in todos:
    if todo['tno']==input_tno:
      print(todo)
      찾았니 = True 
      break
    if 찾았니==False:
      print('할일을 찾을 수 없습니다')
