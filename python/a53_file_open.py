import os


def main():
    print(os.path)
    print(__file__)
    print(os.getcwd())
    os.chdir("/home/lmc/aiot/python/data")
    if os.path.exists("basic.txt"):
        print("파일이 이미 있습니다.")
    else:
        with open('basic.txt', 'w', encoding='utf-8') as file:
            file.write("this is file save data! first\n")
            file.write("this is file save data! second\n")
            

if __name__ == "__main__":
    main()
