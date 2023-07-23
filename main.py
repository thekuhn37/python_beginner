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
# from random import randint, random

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
Method - data에 bound 되는 function. 앞에 data 값 없이 단독으로 호출할 수는 없다.
(특정 데이터에 대하여 어떤 작업을 실행하는(mutate) function의 유형)
name = "NICO"
print(name.replace("O", "a"))
print(name.endswith("O"))
print(name.isupper())
"""

"""
4.1 Lists
"""
"""
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# print(days_of_week.count("Wed"))
# days_of_week.reverse()
print(days_of_week)
days_of_week.append("Sat")
print(days_of_week)
days_of_week.append("Sun")
print(days_of_week)
days_of_week.remove("Sun")
print(days_of_week)
print(days_of_week[2])
print(days_of_week[0])
print(days_of_week[1])
# 리스트 이름 뒤에 []를 입력하면 그 안에 있는 개별 항에 접근할 수 있는데, 그 순서는 인덱스에 따르는데 0부터 시작한다.
# 하나의 리스트 안에 항목들은 모두 동일한 타입일 필요는 없고, 다양할 수 있다.
days_of_week.append([1, 2, 3])
print(days_of_week)
"""

"""
4.4 Recap
TOEICVoca = [{"country": "국가"}, {"war", "전쟁"}, {"determination", "결정"}]
print(TOEICVoca)
TOEICVoca.append({"Beverage": "음료"})
print(TOEICVoca)
print(TOEICVoca[2])

Player = {
    "name": "HDH",
    "Age": "32",
    "Nationality": "Korea",
    "hobby": ["boxing", "running"],
}
print(Player["Nationality"])
Player["hobby"].append("drawing")
print(Player["hobby"])
"""


# 4.5 For Loops

# we can run the code for each item in the sequence(list or tuple) and we can access the item at each cycle.

# 4.6 URL Formatting

# if website.startswith("https://"):
#     print("good to go to", website)
# else:
#     print("we have to fix it")


# 4.7 Request
# sometimes we use module packages which is not included in the standard Pyhthon library.
# "PyPI where you can find modules made by people."

# terminal에서 : pip3 install requests 라치니 requests 설치

# 4.9 Status Code

from requests import get

# get : 웹사이트의 정보를 가져오는 함수

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",
)
# for website in websites:
#     print('The website "', website, '" works properly.')

results = {}


for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    # print(website)

    response = get(website)
    # print(response.status_code)
    # response [200] : the website responded properly.
    if response.status_code == 200:
        # print(f"{website} is okay.")
        results[website] = "OK"
    elif response.status_code > 200 and response.status_code < 300:
        # print(f"{website} is not okay.")
        results[website] = "Fine"
    elif response.status_code >= 300 and response.status_code < 400:
        results[website] = "Not Bad"

print(results)
