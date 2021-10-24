# 구구단
# dan = int(input("몇단을 출력할까요 >>> "))
#
# for number in range(1, 10):
#     string = str(dan) + " * " + str(number) + " ="
#     print(string, dan * number)
while True:
    menuNum = int(input("[메뉴를 입력하세요]\n1.게임시작 2.랭킹보기 3.게임종료 >>>"))
    if menuNum == 1:
        print("-> 게임을시작합니다.")
    elif menuNum == 2:
        print("-> 실시간 랭킹")
    elif menuNum == 3:
        print("게임을 종료합니다.")
        break
    else:
        print("다시 입력하세요")
