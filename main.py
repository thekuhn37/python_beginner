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
