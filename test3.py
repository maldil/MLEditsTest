import numpy

class Test ():
    def add_arrays(self):
        M = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        add = 0
        for x in M:
            add+=x
        sum = add*2
        return sum


if __name__ == "__main__":
    xxx = Test().add_arrays()
    print(xxx)