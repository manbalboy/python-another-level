# 생성자
# : 인스턴스를 만들 때 호출되는 메서드
class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed

    def move(self):
        print("이동하기")


class Wolf(Monster):
    pass


class Shark(Monster):
    def move(self):
        print("헤엄치기")


class Dragon(Monster):
    def move(self):
        print("날기")


wolf = Wolf(100, 20, 20)
print(wolf)

shark = Shark(200, 300, 440)
print(shark)

dragon = Dragon(20049, 299, 200)
print(dragon)

wolf.move()
shark.move()
dragon.move()
