
import numpy

class Test6 ():
    def add_arrays(self):
        H = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        fff = 0
        for a in H:
            fff += a
        cum = fff * 2
        return cum


if __name__ == "__main__":
    xxx = Test6().add_arrays()
    print(xxx)