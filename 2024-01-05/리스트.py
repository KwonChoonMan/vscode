리스트 = [3, 'hello', 5>3, True]
튜플 = tuple(리스트)

# CRUD
# method : 객체(파이썬을 구성하는 부품)에 소속된 함수
리스트.append(100)
리스트[0]=리스트[0]*10
print(리스트)
del 리스트[0]
print(리스트)

# Set - 중복불가능하고 순서가 없다
#       정렬된 것처럼 보야도 우연일 뿐
셋 = {1,2,3,4}
print(셋)
셋.add(5)
print(셋)

# 리스트나 튜플이 중복이가능하고 순서가 있다
리스트 =[1,3,4,6,1,4,2]
set2 = set(리스트)
리스트 = list(set)
print(set2)


