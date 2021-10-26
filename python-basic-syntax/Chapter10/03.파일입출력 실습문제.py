import csv


def changeStockObject(data):
    이름 = data[0]
    매입가 = int(data[1])
    수량 = int(data[2])
    목표가 = int(data[3])

    수익금 = (목표가 - 매입가) * 수량
    수익률 = (목표가 / 매입가 - 1) * 100
    print(f"{이름} : {수익금} : {수익률:.2f}%")


file = open("mystock.csv", "r", newline="", encoding="utf-8-sig")
reader = csv.reader(file)

data = []

for d in reader:
    data.append(d)

file.close()

print(data.__str__())
data = data[1:]
print(data.__str__())

for d in data:
    changeStockObject(d)
