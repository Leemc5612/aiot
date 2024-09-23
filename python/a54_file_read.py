import os


def main():

    print(os.getcwd())
    os.chdir("/home/lmc/aiot/python/data")
    if os.path.exists("basic.txt"):
        with open('basic.txt', 'r', encoding='utf-8') as file:
            # data = file.readline()
            # print(data)
            while(data :=file.readline()):
                print(data, end="")
    else:
        print("파일이 없슈.")
            

if __name__ == "__main__":
    main()
