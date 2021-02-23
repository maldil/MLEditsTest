
import numpy
import tensorflow

class Test6 ():
    def add_arrays(self):
        Q = numpy.ndarray([[1, 2, 3, 4, 5, 6, 7, 8, 9],[1, 2, 3, 4, 5, 6, 7, 8, 9],[1, 2, 3, 4, 5, 6, 7, 8, 9]])
        F = Q*4
        return F

if __name__ == "__main__":
    xxx = Test6().add_arrays()
    print(xxx)