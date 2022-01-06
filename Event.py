import DiceTumble
import System

# 삼진, 그라운드 아웃, 플라이 아웃
# 볼넷, 안타, 2루타, 3루타, 홈런

#아웃카운트
OutCount = 0

inning = int(1)
#초말
top = int(1)
bottom = int(1)
#공격 수비
offense = int(1)
defence = int(1)

#공격 아웃카운트
def OutCountTotal():
    return OutCount
#수비 아웃카운트
def OutCountPlus():
    global OutCount
    OutCount += 1
    if OutCount > 3:
        OutCount = 1
    return OutCount

#공수교대
def OND():
    # global OutCount
    if OutCount == 3:
        print("====공수교대====")


def K():
    print("삼진")
    OCP = OutCountPlus()
    print("아웃 카운트 ", OCP)
    OND()

def GO():
    print("그라운드 아웃")
    OCP = OutCountPlus()
    print("아웃 카운트 ", OCP)
    OND()

def FO():
    print("플라이 아웃")
    OCP = OutCountPlus()
    print("아웃 카운트 ", OCP)
    OND()

def BB():
    print("볼넷")
    OCT = OutCountTotal()
    print("아웃 카운트 ", OCT)

def OneB():
    print("안타")
    OCT = OutCountTotal()
    print("아웃 카운트 ", OCT)

def DoubleB():
    print("2루타")
    OCT = OutCountTotal()
    print("아웃 카운트 ", OCT)

def ThreeB():
    print("3루타")
    OCT = OutCountTotal()
    print("아웃 카운트 ", OCT)

def HR():
    print("홈런")
    OCT = OutCountTotal()
    print("아웃 카운트 ", OCT)


#===========================================================================================

def Result():
    result = DiceTumble.DicePlus()
    if result == 2:
        print(result)
        ThreeB()
    elif result == 3:
        print(result)
        BB()
    elif result == 4:
        print(result)
        DoubleB()
    elif result == 5:
        print(result)
        K()
    elif result == 6:
        print(result)
        GO()
    elif result == 7:
        print(result)
        OneB()
    elif result == 8:
        print(result)
        FO()
    elif result == 9:
        print(result)
        K()
    elif result == 10:
        print(result)
        DoubleB()
    elif result == 11:
        print(result)
        BB()
    elif result == 12:
        print(result)
        HR()