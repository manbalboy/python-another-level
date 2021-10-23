# 문제 1
# money = int(input("현재 가진 금액을 입력  >>>>"))
#
#
# if money >= 20000:
#     print("오늘저녁은 치킨!")
# elif money >= 12000:
#     print("오늘저녁은 떡볶이")
# elif money >= 2000:
#     print("김밥")
# else:
#     print("못먹음")


koreanScore = int(input("국어 >>> "))
mathScore = int(input("수학 >>> "))
englishScore = int(input("영어 >>> "))
average = (koreanScore + mathScore + englishScore) / 3
if (koreanScore > 100 or mathScore > 100 or englishScore > 100) or (
        koreanScore < 0 or mathScore < 0 or englishScore < 0):
    print("점수를 잘 못 입력하였습니다. ");
elif average > 80:
    print("합격입니다.")
else:
    print("불합격입니다.")
