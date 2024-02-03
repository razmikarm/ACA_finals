import numpy as np
from drawer import draw_matrix


class Matrix:
    
    def __init__(self, lst, cell_len):
        self.data = np.array(lst)
        self.cell_len = cell_len + 2

    @property
    def all_zeros(self):
        return np.count_nonzero(self.data) == 0

    def update_cell_len(self):
        vc = np.vectorize(lambda x: len(str(x)))
        max_len = np.max(vc(self.data))
        self.cell_len = max_len

    def draw(self, pre_clear=False, post_pause=False, header=None):
        m, n = self.data.shape
        if header is None:
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
    # if self.all_zeros == True -> homogeneous
    pass


class AugmentedMatrix(Matrix):
    """ [CoefficientMatrix | ConstantMatrix] """

    def __init__(self, coef, const):
        self.data = np.hstack((coef.data, const.data)).astype(float)
        self.cell_len = max(coef.cell_len, const.cell_len)

    def remove_zero_rows(self):
        """ Removing all-zeros rows"""
        prev_shape = self.data.shape
        self.data = self.data[~np.all(self.data == 0, axis=1)]
        if self.data.shape == prev_shape:
            return
        self.draw(
            post_pause=True,
            header="Removed all-zeros row(s):"
        )

    def find_first_non_zero(self, start_idx=0) -> int:
        """ Getting index of first non-zero row"""
        nz = np.argmax(self.data[start_idx:] != 0, axis=1)
        col_idx = np.min(nz)
        col = self.data[start_idx:, col_idx]
        if np.any(col == 1):
            row = np.argmax(col == 1)
        else:
            row = np.nonzero(col)[0][0]
        return row + start_idx, col_idx

    def swap_rows(self, idx1, idx2):
        """Swaping rows of given indices"""
        if idx1 == idx2:
            return
        self.data[[idx1, idx2]] = self.data[[idx2, idx1]]
        self.draw(
            post_pause=True,
            header=f"Interchanged two rows | (R{idx1+1} ↔ R{idx2+1}): "
        )

    def multiply_row(self, idx, scalar, in_place=True):
        if scalar == 1:
            return self.data[idx]
        result = self.data[idx] * scalar
        if not in_place:
            return result
        self.data[idx] = result
        self.update_cell_len()
        self.draw(
            post_pause=True,
            header=(
                "Multiplied a row by a non-zero constant | "
                f"({(scalar:.5f).rstrip('0')} * R{idx+1}): "
            ),
        )

    def add_mul_to_row(self, target_idx, src_idx, scalar):
        header = (
            "Added a multiple of a row to another row | "
            f"(R{target_idx+1} + ({scalar}) · R{src_idx+1}): "
        )
        new_row = self.multiply_row(src_idx, scalar, in_place=False)
        self.data[target_idx] += new_row
        self.update_cell_len()
        self.draw(
            post_pause=True,
            header=header,
        )


