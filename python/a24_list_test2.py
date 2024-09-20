def main():
    list_a = [1, 2, 3]
    print(list_a)
    
    # append 추가
    list_a.append(4) 
    list_a.append(5) 
    print(list_a)

    #insert 삽입 
    list_a.insert(0, 0)
    list_a.insert(3, 2.5)   #3자리에 2.5를 추가해라
    print(list_a)

    #del 제거 
    del list_a[0]
    print(list_a)
    a = "a variable"
    list_a.insert(0, a)
    print(list_a)
    del list_a[0]  #리스트에서만 지워질뿐 메모리가 지워지는건 아님.
    #print(list_a)
    #print(a) #a변수는 사라지지않는다 

    #pop 리스트 맨마지막 요소 리턴하고 그요소 삭제하기
    list_a.append("last element")
    re = list_a.pop(2)
    print(list_a, re)

    #remove 제거 값을 비교해서 제거
    list_a.remove("last element")
    print(list_a)


    
if __name__ == "__main__":
    main()

