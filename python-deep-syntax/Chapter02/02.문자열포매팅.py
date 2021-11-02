name = '기준'
duration = 7

message = name + '님 수강 기간이' + str(duration) + '일 남았습니다.'
print(message)

# 문자열 포매팅 사용시!!!
message_format = f'{name}님 수강기간이 {duration} 일 남았습니다.'
print(message_format)

# format 메서드 사용
a = 'Hello {0} {1} {2}'.format('apple', 'pineapple', 'pen')
print(a)
b = 'Hello {} {} {}'.format('apple', 'pineapple', 'pen')
print(b)
