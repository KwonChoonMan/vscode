# 75,80,70이라는 국어 점수가 있다 - >  집합 타입(sequence)
# 값 하나를 저장 : int , float , str , bool
# 값 여러개를 저장: list , tuple , dictionary , set

kor1= 75
kor2= 80
kor3= 70
print(kor1)              # -----> 값을 하나를 저장하는 별개의 공식
print(kor2)
print(kor3)



# kor의 타입 출력 (list)


kor = [75,80,70]
print(type(kor))                           #  ---> list[   ] (타입)
print(kor[0])                              # 값을 여러개를 저장하기위해 list[  ]를 사용한다 
print(kor[1])
print(kor[2])



# 조건문 , 반복문 
# kor 리스트의 원소를 하나씩 꺼내서 item에 담는다


kor = [75,80,70]
for item in kor:              #  반복문을 사용하여 간략하게 만들 수 있다. 
 print(item)


# 리스트는 [  ] , 튜플은 ( )  
# 리스트는 변경가능하고, 튜플은 변경불가능

리스트 =["사과", "귤", "수박"]
for a in 리스트:
    print(a)
튜플 = ("사과", "귤", "수박")       
for a in 튜플: 
    print(a)

 # Create Real Update Delete 

a ='34'
b = int(a) # 34
c = float(a) # 34.0
d = str(b)  # '34'

ar =[30,40,50,]
ar.append(45) 
print(ar)


# ar을 튜플로 변환해 br에 저장하시오

br = tuple(ar)





# xr에 40을 추가한 다음 출력하시오

xr = (10,20,30)
xr = list(xr)
xr.append(40)
xr= tuple(xr)
print(xr)


