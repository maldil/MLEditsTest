
import numpy
import tensorflow

class Test6 ():
    def add_arrays(self):
        H = numpy.ndarray([[1, 2, 3, 4, 5, 6, 7, 8, 9],[1, 2, 3, 4, 5, 6, 7, 8, 9],[1, 2, 3, 4, 5, 6, 7, 8, 9]])
        B = H*4
        return B

if __name__ == "__main__":
    xxx = Test6().add_arrays()
    print(xxx)