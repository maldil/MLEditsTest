
import numpy

class Test6 ():
    def add_arrays(self):
        B = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        C = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        D = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        A = B+C+D

        L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        jjj = 0
        for a in L:
            jjj += a
        cum = jjj * 2


        P = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        Q = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        R = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        S = P + Q + R

        K = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ttt=0
        for a in K:
            ttt += a

        loo = ttt*100

        return S*cum


if __name__ == "__main__":
    xxx = Test6().add_arrays()
    print(xxx)