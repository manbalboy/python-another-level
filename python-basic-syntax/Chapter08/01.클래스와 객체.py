# 클래스를 사용하는 이유
champion1Name = "이즈리얼"
champion1Health = 700
champion1Attack = 80

print(f"{champion1Name} 님 소환사의 협곡에 오신걸 환영합니다. ")

champion2Name = "리신"
champion2Health = 800
champion2Attack = 95

print(f"{champion2Name} 님 소환사의 협곡에 오신걸 환영합니다. ")


def basicAttackFn(name, attack):
    print(f"{name} 기본공격 {attack}")


basicAttackFn(champion1Name, champion1Attack)
basicAttackFn(champion2Name, champion2Attack)


class Champion:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name} 님 소환사의 협곡에 오신걸 환영합니다.")

    def basicAttackFn(self):
        print(f"{self.name} 기본공격 {self.attack}")


ezreal = Champion("이즈리얼", 700, 90)
leesin = Champion("리신", 800, 95)
yasuo = Champion("야스오", 750, 92)

ezreal.basicAttackFn()
leesin.basicAttackFn()
yasuo.basicAttackFn()
