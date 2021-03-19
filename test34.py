
import numpy

class Test1 ():
    def add_arrays_new(self):
        Z = numpy.ndarray([1, 2, 3, 4, 5, 6, 7, 8, 9])
        bbb = self.sum_array(Z)
        sum = bbb * 2

    def sum_array(self, Z):
        bbb = 0
        for y in Z:
            bbb += y
        return bbb


if __name__ == "__main__":
    xxx = Test1().add_arrays_new()
    print(xxx)



