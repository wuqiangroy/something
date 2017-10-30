class Demo:

    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args

if __name__ == "__main__":
    print(Demo.klassmeth())
    print(Demo.klassmeth("sapm"))
    print(Demo.statmeth())
    print(Demo.statmeth("spam"))