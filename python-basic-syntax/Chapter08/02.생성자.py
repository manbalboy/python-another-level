# 생성자
# : 인스턴스를 만들 때 호출되는 메서드
class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed


wolf = Monster(100, 20, 20)
print(wolf.health)
