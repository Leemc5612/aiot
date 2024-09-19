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

def solution(my_string, is_suffix):
    my_string = my_string.index(is_suffix)
    return my_string






