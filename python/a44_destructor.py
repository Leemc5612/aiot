class Test:

    def __init__(self, name):
        self.name = name
        print(f"{self.name} - 초기화.")

    def __del__(self):
        print(f"{self.name} - 파괴.")

def main():
    a = Test("name")

if __name__ == "__main__":
    main()
