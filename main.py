# my_name = "nico"
# a = 12
# b = "12"
# print(my_name)
# print(a)
# print(b)
# # 숫자가 변수의 제일 앞에 와선 안되고, 변수 내에서 띄어쓰기가 있어서는 안된다.
# answer = False
# # True or False. Boolean의 경우 첫 글자는 무조건 대문자.
# def hotelroom(days):
#     return 350 * days
# def stay(days):
#     return 200 * days
# def tripfee(a, b):
#     return a + b
# room = hotelroom(3)
# travel = stay(3)
# totalfee = tripfee(room, travel)
# if totalfee <= 5000:
#     print(f"Your total fee is {totalfee}. It is appropriate. So it is admitted.")

# Basic!
# 함수 : function (parameter). / 파라미터가 들어가기 위해 선언하는 변수 : variable
# 함수 호출 시 집어넣는 값 : argument // 함수가 돌려보내는 (return) 값 : value


# 2.4 Python Standard Library
from random import randint, random

# phython standard library 의 random module에서 randint 함수(function)를 호출

user_choice = int(input("Choose number."))
pc_choice = randint(1, 100)

if user_choice == pc_choice:
    print("You Won!")
elif user_choice > pc_choice:
    print("Lower! PC chose", pc_choice)
elif user_choice < pc_choice:
    print("Higher! PC chose", pc_choice)
