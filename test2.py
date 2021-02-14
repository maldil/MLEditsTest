import numpy as np

class Test ():
    def add_arrays(self,):
        M = [[1,2,3],[4,5,6],[7,8,9]]
        result= np.sum(np.array(M),axis=1)
        return result