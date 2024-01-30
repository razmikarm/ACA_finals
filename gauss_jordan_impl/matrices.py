import numpy as np


class Matrix:
    
    def __init__(self, lst):
        self.data = np.array(lst)


class CoefficientMatrix(Matrix):
    pass


class ConstantMatrix(Matrix):
    # homogeneous if all() == 0
    pass


# [CoefficientMatrix | ConstantMatrix]
class AugmentedMatrix(Matrix):
    pass
