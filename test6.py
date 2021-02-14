
import numpy

class Test6 ():
    def add_arrays(self):
        Q = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ccc = numpy.sum(Q)
        result=ccc*2
        return result


if __name__ == "__main__":
    xxx = Test6().add_arrays()
    print(xxx)