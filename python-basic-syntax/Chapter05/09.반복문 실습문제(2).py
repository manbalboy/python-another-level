# # 실습문제
# # Learning korean
#
#
# # 한국어리스트
# wordList = ["사랑해", "귀엽다", "고마워", "행복해"]
# print("Let`s Learning Korean")
# for word in wordList:
#     print(word)
#     inputData = input()
#     if word != inputData:
#         break

# 한국어리스트
wordList = ["사랑해", "귀엽다", "고마워", "행복해"]
passWords = []
failWords = []
print("Let`s Learning Korean")
for word in wordList:
    print(word)
    inputData = input()
    if word == inputData:
        passWords.append(word)
    else:
        failWords.append(word)

print("전체 문제 개수 : ", len(word))
print("맞은 문제 개수 : ", len(passWords))
print("틀린 문제 개수 : ", len(failWords))
