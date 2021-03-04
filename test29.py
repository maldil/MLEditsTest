import numpy
import tensorflow

class Test6 ():
    def add_arrays(self):
        data = 0
        boo= [3,4,5]
        collection = [1,2,4,5,6]
        xx=0
        for x in collection:
            if x in boo:
                xx+=x
        return data
    def add_arrays1(self):
        data = 0
        boo= [3,4,5]
        collection1 = [1,2,4,5,6]
        yy=0
        for x in collection1:
            if x in boo:
                yy += x
        return data

    def add_arrays3(self):
        data = 0
        boo= [3,4,5]
        collection3 = [1,2,4,5,6]
        rr=0
        for x in collection3:
            if x in boo:
                rr += x
        return data

    def add_arrays4(self):
        data = 0
        fff= [3,4,5]
        collection4 = [1,2,4,5,6]
        rr=0
        for x in collection4:
            if x in fff:
                rr += x
        return data


if __name__ == "__main__":
    xxx = Test6().add_arrays()
    print(xxx)