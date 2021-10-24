# 기본형

# 1. 정의하기
import numbers


def printHello(name: object) -> object:
    print(name, "님 환영합니다.")


printHello("정훈")
printHello("정윤혜")


def sum(a: numbers, b: numbers) -> None:
    print(a + b)


sum(3, 4)


def add(a, b):
    return a + b


addResult = add(1, 2)
print(addResult)
