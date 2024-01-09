# len 쓰지말고 길이를 내가 측정해보자 
"""
리스트 = [10,20,30,40]
print(len(리스트))
length=0
for item in 리스트:
   length+=1
print(length)

"""
# slicing
리스트 = [10,20,30,40,50]
# 리스트[시작 인덱스: 끝인덱스+1]
print(리스트[0:2]) 
print(리스트[1:4])

# slicing은 문자열도 가능
string = "0123456"
print(string[1:3])
print(string[2:5])

# 간격지정
print(string[3:7])

#string에서 홀수 문자를 출력
print(string[1::2])