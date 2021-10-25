# 결제 정보, 관리모듈
# 변수
version = 2.0


# 함수
def printAuthor():
    print("스타트코딩")


# 클래스
class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time

    def getPayInfo(self):
        return f"{self.time} {self.id} {self.price}"
