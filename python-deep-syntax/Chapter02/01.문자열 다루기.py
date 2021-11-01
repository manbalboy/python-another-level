# 1.replace
# 문자열 교체

replaceStr = '오늘 날씨는 흐림 입니다.'.replace("흐림", "맑음")
print(replaceStr)

# 2. find
# 문자열 찾기

findStrIndex = 'Hello world'.find("l");
print(findStrIndex)

# 3. split
# 문자열 분리

splitStrArr = '나이키 신발 260 x1212'.split()
print(splitStrArr)

# 4.strip
# 문자열 공백 제거
lstripStr = '           Y         '.lstrip()
rstripStr = '           Y         '.rstrip()
stripStr = '       Y           '.strip()

print(lstripStr, "1")
print("1", rstripStr)
print("1", stripStr, "1")
