
import numpy
import tensorflow

class Test6 ():
    def add_arrays(self):
        data={3,4}
        collection = [1, 2, 2, 3]
        for elem in collection:
            data.add(elem)
        return data
if __name__ == "__main__":
    xxx = Test6().add_arrays()
    print(xxx)