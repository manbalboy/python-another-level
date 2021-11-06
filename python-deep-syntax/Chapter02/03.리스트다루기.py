# 리스트 메서드

# 리스트 데이터 삭제

fruits = ['apple', 'banana', 'orange']
print("==============================")
print(fruits.pop());
print(fruits)
print("==============================")
del fruits[0]
print(fruits)
print("==============================")
fruits.append('test')
print(fruits)
print("==============================")
fruits.append('test1')
print(fruits)

# enumerate
print("==============================")
for index, item in enumerate(fruits):
    print(index, item)

print("==============================")

for index, item in enumerate(fruits, 1):
    print(index, item)
