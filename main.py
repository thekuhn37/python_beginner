""""
my_name = "nico"
a = 12
b = "12"
print(my_name)
print(a)
print(b)
# 숫자가 변수의 제일 앞에 와선 안되고, 변수 내에서 띄어쓰기가 있어서는 안된다.
answer = False
# True or False. Boolean의 경우 첫 글자는 무조건 대문자.
def hotelroom(days):
    return 350 * days
def stay(days):
    return 200 * days
def tripfee(a, b):
    return a + b
room = hotelroom(3)
travel = stay(3)
totalfee = tripfee(room, travel)
if totalfee <= 5000:
    print(f"Your total fee is {totalfee}. It is appropriate. So it is admitted.")

Basic!
함수 : function (parameter). / 파라미터가 들어가기 위해 선언하는 변수 : variable
함수 호출 시 집어넣는 값 : argument // 함수가 돌려보내는 (return) 값 : value

큰 따옴표 세개 *2 => 그 사이에 내용은 주석처리 된다.
"""


# 3.4 Python Standard Library
from random import randint, random

# phython standard library 의 random module에서 randint 함수(function)를 호출
"""
print("Welcome to Python Casino")
pc_choice = randint(1, 50)
playing = True

while playing:
    user_choice = int(input("Choose number(1-50):"))
    if user_choice == pc_choice:
        print("You Won!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher!")
"""

""""
[while문]
i = 1
while i <= 10:
    print(f"i is {i}")
    i = i + 1
# while 뒤에 따라오는 조건문(condition)이 참인 동안, 그 뒤에 결과 행동이 반복적으로 실행된다.
"""


# 4. Data Structures
"""
4.0 Methods 
Method - data에 bound 되는 function. (특정 데이터에 대하여 어떤 작업을 실행하는 function의 유형)
"""
name = "NICO"
print(name.replace("O", "a"))
print(name.endswith("O"))
print(name.isupper())
