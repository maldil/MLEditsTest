
import numpy

class Test1 ():
    def add_arrays(self):
        Z = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        aaa = numpy.sum(Z)
        mult = aaa*2
        return mult


if __name__ == "__main__":
    xxx = Test1().add_arrays()
    print(xxx)