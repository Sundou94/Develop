# import random

# ans = random.randint(1, 100)

# print("1 - 100 사이의 렌덤한 숫자를 맞춰보세요")
# a = int(input())
# i = 0

# while True:
#     i += 1
#     if a == ans:
#         print("축하합니다, 정답입니다!! 총 ",i,"번 만에 찾았습니다")
#         break
#     elif a > ans:
#         print("입력하신 값은 정답보다 큼니다 : 다시입력하세요")
#         a = int(input())
#     else:
#         print("입력하신 값은 정답보다 작습니다 : 다시입력하세요")
#         a = int(input())


# def asterisk_test(*args):
#     x, y, *z = args
#     return x, y, z

# print(asterisk_test(3,4,5,10,20))

# 언패킹
# 패킹은 한변수에 여러개의 데이터를 할당하는 것
# 언패킹은 한변수에 여러개의 데이터가 들어 있을 때 그것을 각각의 변수로 반환하는 방법이다.




user_info = {'id' : '1', 'name' : 'hong kildong', 'email' : 'hong@mail.com', 'hp_num' : '010-2343-9160'}
user_info2 = {'id' : '2', 'name' : 'lee soonsin', 'email' : 'lee@mail.com', 'hp_num' : '010-3123-2370'} 
user_info3 = {'id' : '3', 'name' : 'jang youngsil', 'email' : 'jang@mail.com', 'hp_num' : '010-4242-9450'}
user_info4 = {'id' : '4', 'name' : 'king sejong', 'email' : 'king@mail.com', 'hp_num' : '010-2543-1270'}
user = [user_info, user_info2, user_info3, user_info4]

for i in user:
    for k,v in i.items():
        print(k,":",v)