import numpy as np
from drawer import draw_matrix


class Matrix:
    
    def __init__(self, lst, cell_len):
        self.data = np.array(lst)
        self.cell_len = cell_len + 2

    def draw(self, pre_clear=False, post_pause=False):
        m, n = self.data.shape
        header = f"{self.__class__.__name__} :"
        draw_matrix(
            self.data,
            m, n,
            self.cell_len,
            pre_clear=pre_clear,
            post_pause=post_pause,
            header=header,
        )


class CoefficientMatrix(Matrix):
    pass


class ConstantMatrix(Matrix):
    # homogeneous if all() == 0
    pass


class AugmentedMatrix(Matrix):
    """ [CoefficientMatrix | ConstantMatrix] """

    def __init__(self, coef, const):
        self.data = np.hstack((coef.data, const.data))
        self.cell_len = max(coef.cell_len, const.cell_len)
