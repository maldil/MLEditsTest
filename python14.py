
import numpy
import tensorflow

class Test6 ():
    def add_arrays(self):
        L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ddd = 0
        for a in L:
            ddd += a
        cum = ddd * 2


        W = numpy.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],[1, 2, 3, 4, 5, 6, 7, 8, 9],[1, 2, 3, 4, 5, 6, 7, 8, 9]])

        ooo =0
        for a in W:
            ooo += a

        loo = ooo*100

        return loo


if __name__ == "__main__":
    xxx = Test6().add_arrays()
    print(xxx)