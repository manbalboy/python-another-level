import random

lottoNums = []


def getRandomNumber():
    number = random.randint(1, 45)
    return number


def getIsDup(number):
    if number in lottoNums:
        return True
    else:
        return False


while len(lottoNums) < 6:
    number = getRandomNumber()
    if len(lottoNums) == 0 or not getIsDup(number):
        lottoNums.append(number)

lottoNums.sort()
print(lottoNums)
