# 1에서 10까지 합계 : 55
"""
result = 0
for x in range(1,11):
  result=result+x
 print(result)

"""

# 1에서 10까지의 3의 배수 출력
"""
for x in range(1,11):
   if x%3==0:
      print(x)



# continue 활용 
for x in range(1,11):
    if x%3!=0: 
     continue     # continue는 반복을 스킵  # break는 반복을 중단
    print(x)

"""
# 1~10사이의 3의 배수의 합계 -> 3 6 9
"""
result = 0
for x in range(1,11):
    if x%3==0:
      result=result+x
print(result)

"""
# 1~100사이의 5과 7의 공배수를 출력

"""
for x in range (1,101):
    if x%5==0 and x%7==0:
     print(x)

"""
# 1~100사이의 5의 배수와 7의 배수를 출력.  공배수는 제외
"""
for x in range(1,101):
   if x%5==0 or x%7==0:
      print(x)
   elif x%5==0 and x%7==0:
      print(x)
"""
for i in range(1,101):
    if i%5==0 and i%7==0:
        continue
    if i%5==0 or i%7==0:
        print(i,end=" ")
    
        




        