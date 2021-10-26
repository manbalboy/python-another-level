# # 1. 파일 쓰기
# file = open("data.txt", "w", encoding="utf8")
# file.write("1. 스타트코딩과 함께 파이썬 공부")
# file.close()
#
# # 2. 파일추가
# file = open("data.txt", "a", encoding="utf8")
# file.write("\n2. 스타트코딩과 함께 파이썬 공부")
# file.close()

# 3. 파일 읽기
# 3.1 파일 전체 읽기
file = open("data.txt", "r", encoding="utf8")
data = file.read()
print(data)
file.close()
print("///////////////////////////////////")
# 3.2 파일 한줄 읽기
file = open("data.txt", "r", encoding="utf8")
while True:
    data = file.readline()
    print(data)
    if data == "":
        break
file.close()
