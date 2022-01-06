import random
import DiceTumble
import System
import os
import time
#두 개의 주사위를 던진다.

#이닝
import Event
inning = int(1)


print("--------------------")
print("경기 시작 합니다.")
print("--------------------")
print(f"{inning}회 ")
print("--------------------")
for i in range(1,30):
    time.sleep(3)
    print(i, "번")
    Event.Result()
    print("--------------------")


# 어떤수 나오니
# print("D1은",DiceTumble.Dice1())
# print("D2는",DiceTumble.Dice2())
# print("합은",DiceTumble.DicePlus())


# D1ranChoice = random.choice(D1)
# D2ranChoice = random.choice(D2)

###################################################################
# while inning <= 200:
#     D1ranChoice = random.choice(D1)
#     D2ranChoice = random.choice(D2)
#     if current_price == 0:
#         break
#
#     if ranChoice == 0:
#         current_price = current_price - 1
#         #print('-1p')
#         print(current_price)
#     elif ranChoice == 1:
#         current_price = current_price + 0
#         #print('0p')
#         print(current_price)
#     elif ranChoice == 2:
#         current_price = current_price + 1
#         #print('+1p')
#         print(current_price)
