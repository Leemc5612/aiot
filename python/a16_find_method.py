def main():
    output_a = 0
    while output_a != -1:
        output_a = "안녕안녕하세요.".find("안녕", output_a+1)
        print(output_a)

    a = "10 20 30 40 50".split()
    print(a)
    str1 = " ".join(a)
    print(str1)
    
if __name__ == "__main__":
    main()
