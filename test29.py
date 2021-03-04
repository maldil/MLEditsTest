import numpy
import tensorflow

class Test6 ():
    def add_arrays(self):
        data = 0
        boo= [3,4,5]
        collection = [1,2,4,5,6]
        xx=0
        for x in collection:
            xx+=x
        return data


if __name__ == "__main__":
    xxx = Test6().add_arrays()
    print(xxx)