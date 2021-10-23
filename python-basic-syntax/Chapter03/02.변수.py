# 변수
# 변수이름 = 데이터


# 마스터이 챔피언 데이터를 변수에 저장
name = "마스터이"
level = 5
health = 800
attack = 90

print("origin : " + name, level, health, attack, sep=", ")

# 변수에 저장된 데이터를 변경하기
level = 6
health = 850
attack = 100

print("change : " + name, level, health, attack, sep=", ")

level = level + 1
health = 850
attack = 100

print("change : " + name, level, health, attack, sep=", ")
