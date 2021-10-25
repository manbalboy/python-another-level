# 내장모듈
# : 파이썬 설치시 자동으로 설치되는 모듈
import math
from math import pi, ceil as c  # static import

print(pi)
print(c(2.7))
print(math.log(1))

# 외부 모듈
# : 다른 사람이 만든 파이썬 파일 pip (pip install pyautogui)
import pyautogui as pg

pg.moveTo(500, 500, duration=2)
