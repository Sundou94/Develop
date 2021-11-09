## 1

print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(5*3)
print(3*3+1)
print(3*(3+1))

## 2

print('풍선')
print('나비')
print('와'*5)

## 3 참/ 거짓

print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not (5 < 10))

## 4 변수

age = 4
animal = "고양이"
name = "해피"
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) + "살이며, 산책을 아주 좋아해요")
print(name + "어른일까요?" + str(is_adult))

# str 정수형일때 사용 + 대신 , 을 사용하면 빈칸이 들어가며 str 사용하지 않아도 됨

## 주석

'''작은 따움표 
3개 사용시 여러문장
주석이 가능합니다'''

# 드레그 후 command + / 하면 주석이다

print(1+1)
print(3-1)
print(5*2)
print(2**3) # 2^3=8
print(5%3) # 나머지 %
print(10//3) # 몫 //
print(4 >= 7) # 크거나 같다
print(3==3) # == 같다
print(1!=3) # != 같지않다
print(not(1 != 3)) #not은 뒤집는 것

print((3>0) | (3>2)) # | = or , & = and

## 간단한 수식

number = 1
print(number)
number += 2 ## += 자기자신에 더하기
print(number)
number *= 3 ## 자기 자신에 곱하기, -, /, %)

## 숫자처리 함수

#abs 절댓값
print(abs(-5))

#pow 승
print(pow(4,2))

#max 최댓값 반환
print(max(5, 12))

#min 최솟값 반환
print(min(5,12))

#round 반올림
print(round(3.14))

from math import * # 수학 라이브러리 사용
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #근



from  random import * # 랜덤 라이브러리

print(random()) # 난수 사용 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 마만의 임의의 값 생성
print(int(random() * 10)) # 정수만 생성
print(int(random() *10 + 1)) # 1부터 10이하의 값 생성 10 포함 0 제외

#로또 생성기 ㅋㅋ
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

jumin = "940301-1409111"

print(("성별 : " + jumin[7]))
print("연도 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6]) ## [] 문자열 INDEX, [x:y] x부터 y까지 , [x:] x부터 끝까지. -가 붙으면 뒤에서부터

# 문자열 끝까지

python = "Python is Amazing"
print(python.lower())  # 모든문자 소문자로
print(python.upper())  # 모든문자 대문자로
print(python[0].isupper())  # x변수가 대문자인지?
print(len(python))  # 길이가 얼마인지?
print(python.replace("Python","Java"))  # replace() 문자열 교체

index = python.index("n")
print(index)  # n 이라는 글자가 어디인지?

index = python.index("n", index + 1)  # 두번째 n을 찾을때
print(index)

print(python.find("n"))

print(python.find("java"))  # 원하는 값이 없을경우 "-1"반환 index 함수는 error 발생

# 문자열

# 방법 1
print("나는 %d살 입니다." % 20)  # d는 정수 % 정수가들어간다
print("나는 %s를 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % "A")

# s를 넣으면 숫자도 가능
print("나는 %s 입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("빨간", "파란"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

# 방법 3
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")  # print(f"{}") 폼사용시 외부 변수 사용가능


# 문자열 (탈출문자)
print("백문이 불여일견 \n 백견이 불여일타") # \n 줄바꿈
print('저는 "선도우"입니다')
print("저는 \"선도우\" 입니다.") # 역슬러쉬는 그냥 문자열로 인식해줌

# \\ : 문장내에서 \ (파일경로 표시할 때 사용)

# \r : 커서를 맨앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭 키와 동일

site = "http://navr.com"

site = site[7:]
print(site)

index = site.index(".")
site = site[:index]
print(site)

pswd_1 = site[0:3]
pswd_2 = len(site)
pswd_3 = site.count("e")
print(f"생성된 비밀번호 : {pswd_1}{pswd_2}{pswd_3}!")

# 리스트 []

subway = ["유제석", "조세호", "박명수"]
print(subway)

# 조세호씨는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 넣음
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 꺼냄
print(subway.pop()) # 뒤에서 부터 뺌
print(subway)

# 정렬하기

num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 반대로 정렬
num_list.reverse()
print(num_list)


# 다지우고 싶어 .clear
# num_list.clear()
# print(num_list)


# 다양한 자료형 함께 사용가능
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장 가능
num_list.extend(mix_list)
print(num_list)

## 사전

# 사전은 {} 중괄호 사용 {키값 : "내용"}
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
# 대괄호로 key 값 호출

print(cabinet.get(3))
# .get()로 호출 가능

print(cabinet.get(5))
# []이용 호출 할시 없는 경우 오류 발생
# get()이용 시 없는 경우 none 호출

print(3 in cabinet)
print(5 in cabinet)
# 사전안에 값이 있는지 없는지 확인이 가능하다

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
# 정수형 뿐만아니라 문자열도 가능

cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)
#새로 넣거나 바꿀 수 있다

del cabinet["A-3"]
print(cabinet)
# del로 삭제 가능하다

print(cabinet.keys())
# Key만 출력

print(cabinet.values())
# values만 출력

print(cabinet.items())
# key, values 출력

print(cabinet.clear())
# 전부 지우기

## 튜플

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
# 튜플은 추가하거나 변경이 불가능하다

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

## 집합 (set)
# 중복이 안되고 순서가 없음

my_set = {1,2,3,3,3}
print(my_set)


print("\"!@#$%^&*()\'")

print("\"C:\\Download\\\'hello\'.py\"")

print("print(\"Hello\\nWorld\")")

# for i in range(n) :    #range(n)에 들어있는(in) 각각의 수에 대해서(for) 순서대로 i에 저장해 가면서...
# 이때의 for는 각각의 값에 대하여... 라는 for each 의 의미를 가진다고 생각할 수 있다.
#
# range(끝)
# range(시작, 끝)
# range(시작, 끝, 증감)

# 81
# n = int(input(),16)
# for i in range(1, 16) :
#     gop = n * i
#     print('%X'%n,"*",'%X'%i,"=",'%X'%gop,sep='')


# 82
# n = int(input())
# for i in range(1, n+1) :
#   if i%10==3 or i%10==6 or i%10==9 : #1의 자리 찾기
#     print("X", end=' ')
#   else :
#     print(i, end=' ')


# 83
# r, g, b = input().split()
# cnt = 0
#
# for i in range(0,int(r)) :
#   for j in range(0,int(g)) :
#     for k in range(0,int(b)) :
#       print(i,j,k,sep=' ')
#       cnt += 1
# print(cnt)

# 84
# h, b, c, s = input().split()
# h = int(h)
# b = int(b)
# c = int(c)
# s = int(s)
#
# volume = ( h * b * c * s ) / 8
# MegaVolume = volume/1024/1024
# print("%0.1f" %MegaVolume,"MB")

# 85
# 참고 : round(반올림하고자 하는 값, 자릿수)
# w, h, b = input().split()
# w = int(w)
# h = int(h)
# b = int(b)
#
# volume = ( w * h * b) / 8
# MegaVolume = volume/1024/1024
# print("%0.2f" %round(MegaVolume,2),"MB")

# 86
# n = int(input())
# cnt = 1
# sum = 0
# while True :
#     sum = sum + cnt
#     cnt = cnt + 1
#     if sum >= n :
#         break
#
# print(sum)

# 87
# n = int(input())
# for i in range(1,n+1) :
#     if i%3 == 0 :
#         continue # 다음 단계로 넘어가기
#     print(i,end=' ')

# 88
# a, d, n = input().split()
# a = int(a)
# d = int(d)
# n = int(n)
# r = a
# c = 1
# while True :
#     if(c == n) :
#         print(r)
#         break
#     r = r + d
#     c = c + 1


# print("\\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \\(__)|")

# print("|\\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\\\__|")

# a, b =input().split()
# c = int(a) + int(b)
# print(c)

# a, b =input().split()
# c = int(a) - int(b)
# print(c)

# a, b, c=input().split()
# a=int(a)
# b=int(b)
# c=int(c)
#
# print((a+b)%c)
# print(((a%c)+(b%c))%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)

# a=int(input())
# b=input()
#
# print(int(b[2])*a)
# print(int(b[1])*a)
# print(int(b[0])*a)
# print(int(b[2])*a + int(b[1])*a*10 + int(b[0])*a*100)

# 윤년구하기
# yy = int(input())
# if ( (yy%4 == 0) & (yy%100 != 0 ))| (yy%400 == 0):
#     print(1)
# else:
#     print(0)

# a = int(input())
# b = int(input())
#
# if (a > 0) & (b > 0):
#     print(1)
# elif (a > 0) & (b < 0):
#     print(4)
# elif (a < 0) & (b < 0):
#     print(3)
# elif (a < 0) & (b > 0):
#     print(2)

# 알람시계를 사용해 봅시다
# H, M = input().split()
# H = int(H)
# M = int(M)
# if M >= 45:
#     M = M-45
# elif (H != 0)&(M <= 45):
#     M = M+60-45
#     H = H-1
# else:
#     M = M+60-45
#     H = 23
# print(H, M)

# 구구단
# N = int(input())
# for i in range(1,10):
#     r = N*i
#     print(N,"*",i,"=",r)

# A+B
# T = int(input())
# for i in range(0,T):
#     a, b = input().split()
#     a = int(a)
#     b = int(b)
#     print(a + b)




