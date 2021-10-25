# 생성자
# : 인스턴스를 만들 때 호출되는 메서드
import random


class Monster:
    max_num = 1000

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1

    def move(self):
        print("이동하기")


class Wolf(Monster):
    pass


class Shark(Monster):
    def move(self):
        print("헤엄치기")


class Dragon(Monster):
    # 생성자 오버라이딩
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ("불뿜기", "꼬리치기", "날개치기")

    def move(self):
        print("날기")

    def skill(self):
        print(f"{self.name} 스킬사용 {self.skills[random.randint(0, 2)]}")


dragon = Dragon("드래곤", 299, 200)
dragon.skill()
dragon.skill()
dragon.skill()
dragon.skill()
dragon.skill()
