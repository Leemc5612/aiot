# jumin = "990120-1234567"#필요한만큼 잘라서 쓰는걸 슬라이씽

# # print("성별 : " + jumin[7])
# # print("년 : " + jumin[0:2]) #0부터 2직전까지 0,1
# # print("월 : " + jumin[2:4])
# # print("일 : " + jumin[4:6])

# print("생년원일 : " + jumin[:6])# 처음부터 6직전까지 값 0 생략가능
# print("뒤 7자리 : " + jumin[7:])# 7번째부터 끝까지 끝번호 생략가능
# print("뒤7자리 (뒤에부터) : " + jumin[-7:])#맨뒤에서 7번째 부터 끝까지

# #문자열 처리함수

# python = "Python is Amazing"
# print(python.lower()) #소문자로만 출력
# print(python.upper()) #대문자로만 출력
# print(python[0].isupper())#첫번째값이 대문자인지 확인하기 
# print(len(python)) #문자열 길이 반환
# print(python.replace("Python", "Java")) #파이썬을 찾아서 자바로 바꾸기

# index = python.index("n") #n의 위치 찾기
# print(index)
# index = python.index("n", index + 1)#그담에 나오는 두번째 n을찾는다
# print(index)

# print(python.find("Java"))

# print(python.count("n")) #n이 몇번 나오는지 찾는 함수

#문자열 format

# print("a" + "b")
# print("a", "b")

#방법 1
# print("나는 %d살입니다." %20)
# print("나는 %s을 좋아해요" %"파이썬")
# print("Apple 은 %c로 시작해요."%"A")
# # %s
# print("나는 %s살입니다." %20)
# print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

#방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# #방법 3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간"))

#방법 4 (v3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")

#탈출문자

# print("백문이 불여일견\n백견이 불여일타")

# 저는 "나도 코딩" 입니다.
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.") #역슬래쉬를 적으면됨 ""안에 ""

# \\ : 문장 내에서 \ 하나로 바뀜

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스 역활(한글자 삭제)
# print("Redd\bApple")

# \t :  4~8 움직이는 탭


# ur1 = "http://google.com"
# my_str = ur1.replace("http://", "") # 규칙 1

# my_str = my_str[:my_str.index(".")] # 규칙 2

# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1} 입니다".format(ur1, password))

# def solution(my_string, is_suffix):
#     my_string = my_string.index(is_suffix)
#     return my_string

# 리스트 

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)
# print(subway.index("조세호"))

# print(subway)

# #딕셔너리 자료형
# cabinet = {3:"유재석", 100:"김태호"}
# # print(cabinet[3])
# # print(cabinet[100])

# # print(cabinet.get(3))
# # # print(cabinet[5])
# # print(cabinet.get(5))
# # print(cabinet.get(5, "사용 가능"))

# # print("hi")

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# # cabinet = {"A-3": "유재석", "B_100":"김태호"}
# # print(cabinet["A-3"])
# # print(cabinet["B_100"])

# # # 새 손님
# # print(cabinet)
# # cabinet["A-3"] = "김종국"
# # cabinet["C-20"] = "조세호"
# # print(cabinet)

# # 튜플

# # meun = ("돈까스", "치즈까스")
# # print(meun[0])
# # print(meun[1])

# # name = "김종국"
# # age = 20
# # hobby = "코딩"
# # print(name, age, hobby)

# # (name, age, hobby) =  ("김종국", 20, "코딩")
# # print(name, age, hobby)

# #집합 (set)
# # 중복 안됨, 순서 없음

# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (java와 python 을 모두 할수 잇ㄴ는 개발자)

# print(java & python)
# print(java.intersection(python))

# # 합집합(java python 하나라도 할수있는 개발자)
# print(java | python)
# print(java.union(python))

# #차집합( java 하수있지만 python은 할줄ㅇ 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# #python 할줄아는 사람이 늘어났다
# python.add("김태호")
# print(python)

# #java를 까먹음

# java.remove("김태호")
# print(java)


#자료 구조의 변경
#커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))


