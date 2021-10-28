# raise 구문을 사용해서 에러를 강제로 발생
num = int(input("음수를 입력해주세요"))


class HunError(Exception):
    def __init__(self):
        super().__init__("양수는 입력불가")


try:
    if num >= 0:
        raise HunError
except HunError as e:
    print(e)
