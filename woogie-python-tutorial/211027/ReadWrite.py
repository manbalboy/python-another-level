open ('a.txt','w') # 파일을 열어라. 없으면 'w'rite해라.(만들어라)

file = open('a.txt','w') # file이라는 변수에다가 대입도 됨. 이미 있으면 덮어쓰기 됨

file.write('hello')

file.write(' plus!')

file.write('add')

file = open('a.txt', 'a') # file을 append모드로 오픈함.


# file.close() # close를 안해주면 에러난다고 하는데 일단 되긴함.

file = open('a.txt','r') # read모드로 파일을 오픈한거임

print(file.read()) # 그러면 이렇게 출력이됨

file.close() # 열었으면 닫아주자.

excelFile = open('data.csv', 'w') # excel파일을 만들려면 .csv로 파일을 써보자

excelFile.write('김,이,박')
excelFile.write('\n1,2,3') #\n이 파이썬에서 엔터키임. 띄워서 두줄만들고싶으면 이렇게 함

# 일단 근데 무슨 무슨 모드 도킹! 이딴 거 안해도 다 되긴함.
