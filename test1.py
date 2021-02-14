import numpy as np

class Test():
    def set_hyperparameters(self,length_scale):
        self.length_scale = np.size(length_scale)
        return self.length_scale
    def main(self):
        test = Test()
        length = test.set_hyperparameters([1,2,3,4])
        print(length)

def add_arrays():
    length = np.len([1,2,4])
    final_length =  np.power(4,length)
