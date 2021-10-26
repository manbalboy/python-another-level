
# q1.
list = ['삼성전자','카카오','네이버','신풍제약'] 
# 해당 리스트를 txt파일로 저장하려면?

# answer 1.
q1 = open('question1.txt','w',encoding="utf-8") # encoding-utf-8을 붙여주면 utf8로 인코딩도 함 굳

for i in list:
    q1.write(i + '\n')

q1.close();

# q2.
# 구구단 결과 값 출력을 해보려면?

# answer2.

for i in range(2,10):
    for j in range(1,10):
        print(i*j)