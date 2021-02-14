
import numpy

class Test6 ():
    def add_arrays(self):
        F = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        add = numpy.sum(F)
        cum = add*2
        return cum


if __name__ == "__main__":
    xxx = Test6().add_arrays()
    print(xxx)