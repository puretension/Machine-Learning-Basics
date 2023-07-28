# print("Python", "Java","Swift",sep=" vs ")

# print("Python", "Java", "C++", "Swift",sep=",", end = "?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file = sys.stdout)
# print("Python", "Java", file = sys.stderr) # error 

# # 정형화된 출력
# scores = {"math": 80, "eng": 60, "coding": 100}
# for subject, score in scores.items():
#     print(subject.ljust(8),str(score).rjust(4),sep= ":")

# 은행 대기순번표 001 002..

# for num in range(1,21):
#     print("대기번호: " + str(num).zfill(3))

# answer = input("아무값이나 입력하세요!: ")
# print("printed: " + answer)
# print("입력하신 값은 " + answer + "입니다.")

# sentence = input()
# print(sentence.split(",")[0])

# # blank space 만큼 10자리 확보하여 format()출력
# print("{0: >10}".format(500))
# # 양수일땐 + 표시, 음수일땐 - 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽정렬후 빈칸으로 _ 채운다
# print("{0:_<10}".format(500))
# # 3자리마다 콤마 찍어주고, 부호도 붙이기
# print("{0:,}".format(100000000000))
# print("{0:+,}".format(100000000000))
# print("{0:+,}".format(-100000000000))
# # 빈자리는 ^로 채우기
# print("{0:^<+30,}".format(100000000000))
# print("{0:f}".format(5/3))
# print("{0:.2f}".format(5/3))

# 파일 입출력
# 덮어쓰기
# score_file = open("score.txt", "w",encoding = "utf8") # write (w는 덮어쓰기)
# print("math : 0", file=score_file)
# print("eng: 50",file=score_file)
# score_file.close()

# 덧붙여쓰기
# score_file = open("score.txt", "a", encoding="utf8") # write(a는 이어서 덧붙이기)
# score_file.write("science: 80")
# score_file.write("\ncoding: 100")

# # 읽기
# score_file = open("score.txt", "r",encoding="utf8") # read 파일읽기
# print(score_file.read())
# score_file.close()

# # 줄별로 읽기
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음줄 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())

# # 파일의 줄을 알고싶을때
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# pickle - pickle에서는 항상 binary 
import pickle 
# w는 쓰기 b는 binary
# profile_file = open("profile.pickle", "wb")
# profile = {"name": "scott", "age": 30, "hobby": ["soccer", "music", "coding"]}
# print(profile)
# # 핵심
# pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file(파일)에 저장
# profile_file.close()

# # 읽기
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile) # {'name': 'scott', 'age': 30, 'hobby': ['soccer', 'music', 'coding']}
# profile_file.close()

# # profile.pickle 파일 열어서 profile_file로 저장한 후 profile_file로 열어주기(load)
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding = "utf8") as study_file:
#     study_file.write("I'm studying python")

# with open("study.txt", "r", encoding = "utf8") as study_file:
#     print(study_file.read())


# Quiz
# 부서 : 
# 이름 : 
# 업무 요약 : 

# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 - ".format(i))
#         report_file.write("부서:")
#         report_file.write("이름:")
#         report_file.write("업무 요약:")

