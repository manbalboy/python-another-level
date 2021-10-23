x = input("첫번째 숫자를 입력하세요 >>> ")
y = input("두번째 숫자를 입력하세요 >>> ")

# 자료형 확인하기 : type(x)
print(type(x), type(y), sep=", ")

print("두개의 숫자를 더한 숫자는 : ", int(x) + int(y))

z = input("태어난 년도를 입력하세요 >>> ")
age = int(2021) - int(z) + 1

print("나이는 " + str(age) + "입니다")

# 정리
# 1. 사용자로 부터 입력받기
# input("입력할 시 출력할 메세지")


# 2. 자료형 변환
# 숫자형으로 변환
# int(데이터)
