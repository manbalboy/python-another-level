# 문제 1
# pushUp = [20, 50, 11, 42, 52]
# print(pushUp)
#
# pushUp.append(55)
# print(pushUp)
#
# pushUp[1] = 30
# print(pushUp)
#
# print(pushUp[1:5])
#
# pushUp.sort()
# print(pushUp)

# 문제 2
pullUp = []
pullUp.append(int(input("1일차 턱걸이 횟수 >>> ")))
pullUp.append(int(input("2일차 턱걸이 횟수 >>> ")))
pullUp.append(int(input("3일차 턱걸이 횟수 >>> ")))
pullUp.append(int(input("4일차 턱걸이 횟수 >>> ")))
pullUp.append(int(input("5일차 턱걸이 횟수 >>> ")))
pullUp.append(int(input("6일차 턱걸이 횟수 >>> ")))
pullUp.append(int(input("7일차 턱걸이 횟수 >>> ")))

totalCount = pullUp[0] + pullUp[1] + pullUp[2] + pullUp[3] + pullUp[4] + pullUp[5] + pullUp[6]
average = totalCount / 7
print(int(average))
