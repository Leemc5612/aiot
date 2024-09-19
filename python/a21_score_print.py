def main():
    score =float(input("학점 입력> "))
 
    if score == 4.5:
        print(f"{score}점 변새롬 등급")
    elif 4.2 <= score < 4.5:
        print(f"{score}점 교수님의 사랑 등급")
    elif 3.5 <= score < 4.2:
        print(f"{score}점 현 체제의 수호자 등급")
    elif 2.8 <= score < 3.5:
        print(f"{score}점 킹반인 등급")
    elif 2.3 <= score < 2.8:
        print(f"{score}점 일탈을 꿈구는 소시민 등급")
    elif 1.75 <= score < 2.3:
        print(f"{score}점 자벌레 등급")
    elif 1.0 <= score < 1.75:
        print(f"{score}점 개벌레 등급")
    elif 0.5 <= score < 1.0:
        print(f"{score}점 현 인생나락 등급")
    elif 0.0 <= score < 0.5:
        print(f"{score}점 자살해라 등급")


if __name__ == "__main__":
    main()

