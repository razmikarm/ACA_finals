from abc import ABC, abstractmethod
import numpy as np


class Matrix(ABC):
    pass


class CoefficientMatrix(Matrix):
    pass


class ConstantMatrix(Matrix):
    # homogeneous if all() == 0
    pass


# [CoefficientMatrix | ConstantMatrix]
class AugmentedMatrix(Matrix):
    pass
