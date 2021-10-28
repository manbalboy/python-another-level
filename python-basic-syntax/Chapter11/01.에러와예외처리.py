# 원화를 입력, 환율 입력  -> 달러값
won = input("원화금액을 입력 하세요 >>>> ")
dollar = input("환율을 입력 하세요 >>>> ")
try:
    # 예외가 발생할 수 있는 코드
    print(int(won) / int(dollar))
except BaseException as e:
    print(e)
else:
    print("예외가 발생하지 않은 코드")
finally:
    print("항상 실행되는 코드 ")

print("끝")
