def multiply(x, y):
    """
    두수의 곱셈 결과를 반환하는 함수
    :param x:  숫자
    :param y:  숫자
    :return:  두수의 곱
    """
    result = x * y
    return result


print(multiply(2, 2))


def printSumAvg(x, y, z):
    """
    세개의 숫자를 받아 합계와 평균을 출력하는 함수
    :param x: 숫자1
    :param y: 숫자2
    :param z: 숫자3
    """
    sum = x + y + z
    avg = sum / 3
    print(f"합계 : {sum} 평균 : {avg}")


printSumAvg(10, 20, 30)
