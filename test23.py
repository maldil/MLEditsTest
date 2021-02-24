import numpy
import tensorflow

class Test6 ():
    def add_arrays(self):
        data = 0
        collection = [1,2,4,5,6]
        for x in collection:
            if (x>2):
                data+=x
        return data


if __name__ == "__main__":
    xxx = Test6().add_arrays()
    print(xxx)