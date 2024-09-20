def main():
    example_list = ['요소A', '요소B', '요소C']

    print(enumerate(example_list))
    for eun in enumerate(example_list):
        print(eun)
        # () = (0, '요소A')
        i, v = eun
        print(f"{i} 번째 원소는 {v} 이다")

if __name__ == "__main__":
    main()
