def main():
    #li1 = []   #리스트 선언
    #li1 = list() #리스트 선언 2
    li1 = [123, 333, 1.2, 'list element']  #선언과 동시 초기화
    print(type(li1))
    print(li1)

    #인덱싱 
    print(li1[0])
    print(li1[1])
    print(li1[2:4])

    #변경

    li1[1] = "삼삼삼"  
    print(li1)

    #리스트 연산자
    list_a = [1,2,3]
    list_b = [4,5,6]

    print(list_a + list_b)
    
    #list_a.extend(list_b)  #메서드
    print(list_a)

    print(list_a * 3)
    print(len(list_a))




if __name__ == "__main__":
    main()
