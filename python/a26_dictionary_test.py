def main():
    # 선업
    dict_a = {'a':123}
    print(type(dict_a))
    set_a = set()
    # set_a.add(1)
    set_b = {1,2,3}
    print(type(set_a))
    print(dict_a, set_a)

    #요소에 접근하기
    dict_a['b'] = 456
    dict_a['a'] = '123'
    print(dict_a)

    #요소 접근
    print(dict_a['a'], dict_a['b'])




if __name__ == "__main__":
    main()
