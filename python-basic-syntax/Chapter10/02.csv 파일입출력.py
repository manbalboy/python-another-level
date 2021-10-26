#
# import pickle
# data = {
#     "목표1": "매일 팔굽혀 펴기 100회",
#     "목표2": "매일 윗몸일으키기 20회",
#     "목표3": "매일 코딩공부 1시간"
# }
#
# file = open("data.pickle", "wb")
# pickle.dump(data, file)
#
# file.close()

# # 가져오기
# file = open("data.pickle", "rb")
# data = pickle.load(file)
# print(data)
# file.close()

# # with 구문을 사용
# with open("data.txt", "r", encoding="utf8") as file:
#     data = file.read()
#     print(data)
import csv

# data = [
#     ["이름", "반", "번호"],
#     ["정훈", "1", "20"],
#     ["훈", "2", "33"],
#     ["후니", "3", "23"],
# ]
#
# file = open("student.csv", "w", newline="", encoding="utf-8-sig")
# writer = csv.writer(file)
#
# for d in data:
#     writer.writerow(d)
#
# file.close()

file = open("student.csv", "r", newline="", encoding="utf-8-sig")
reader = csv.reader(file);
for d in reader:
    print(d)
file.close()
