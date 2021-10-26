중고차 = ['k5','white',5000] # 파이썬의 배열 List

print(중고차[0:3]) # 0에서 3 전까지의 데이터를 뽑아줘요.

중고차[1] = 'black' # 배열의 변수를 유연하게 변경 가능

print(중고차[0:3]) # white가 black으로 변경된거 확인됨

# 중고차.sort() # 숫자 문자순으로 정렬해줌

# 중고차.reverse() # 배열을 거꾸로 뒤집음

# 중고차.pop() # 배열의 끝값 하나를 뿅 가져옴.

중고차2= {'brand': 'BMW','model':'520d'} # 중괄호를 썼으니 Dictionary라고 하는 자료형임

print(중고차2) # Dictionary 자료형은 그 앞에 이름 안적어주면 안됨, 그니까 키값 밸류값 매기는 느낌인것 같음

print(중고차2['brand']) # BMW만 출력되는걸 확인가능.

중고차2['brand'] = 123

print(중고차2['brand']) # 123만 출력되는걸 확인가능.

# List와 Dictionary, 자바의 ArayList와 map에 해당하는 배열 구조인것 같다.

# 근데 진짜 간편하다. 굳!
