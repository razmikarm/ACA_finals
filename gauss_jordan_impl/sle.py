"""
    Gauss-Jordan elimination algorithm:

    Step 1. Carry the augmented matrix [ A|b ] to a reduced row-echelon
            matrix using elementary row operations.
    Step 2. If a row [0 0 0 · · · 0 | 1] occurs, the system is
            inconsistent.
    Step 3. Otherwise, if there are any nonleading variables, assign them
            as parameters (treat them as arbitrary parameters a, b, . . . ).
    Step 4. Use the equations corresponding to the reduced row-echelon
            matrix to solve for the leading variables.

    If at the Step 3 we had no nonleading variables (hence no parameters) we
            will get a unique solution.
"""

import numpy as np
from matrices import CoefficientMatrix, ConstantMatrix, AugmentedMatrix 


# Systems of Linear Equations
class SLE:
    
    def __init__(self, coef, const):
        self.coef = coef
        self.const = const
        self.aug = AugmentedMatrix(self.coef, self.const)
        # elementary row operations
        self.elops = {
            "Interchange two rows | (Ri ↔ Rj)": None,
            "Multiply a row by a non-zero constant | (c · Rj)": None,
            "Add a multiple of a row to another row | (Ri + c · Rj)": None,
        }

    def to_ref(self):
        """
        Transform to row-echelon form

        Step 1. If the matrix consists entirely of zeros, stop.
        Step 2. Otherwise, find the row that contains the leftmost nonzero
                entry of the matrix (call that entry `a`).
        Step 3. Move that row to the top position.
        Step 4. Multiply that row by 1/`a` to create a leading 1.
        Step 5. By subtracting multiples of that row from rows below it,
                make the entries below the leading 1 in that column all 0.
        Step 6. Fix the first row, and repeat steps 1-5 on the matrix
                consisting of the remaining rows (we don't touch the first
                row anymore).
        """

        # Step 1
        if self.aug.all_zeros:
            exit("All values are zeros")

        for r in range(len(self.aug.data)):
            
            # Removing all-zeros rows
            self.aug.remove_zero_rows()

            # Step 2
            nz_row, nz_col = self.aug.find_first_non_zero(start_idx=r)

            #Step 3
            if nz_row != r:
                self.aug.swap_rows(r, nz_row)
            if np.count_nonzero(self.aug.data[nz_row][:-1]) == 0:
                break

            # Step 4
            scalar = 1/self.aug.data[r, nz_col]
            self.aug.multiply_row(r, scalar)

            # Step 5
            for i in range(r + 1, len(self.aug.data)):
                scalar = (-1) * self.aug.data[i, nz_col]
                if scalar == 0:
                    continue
                self.aug.add_mul_to_row(i, r, scalar)
        
        self.aug.draw(
            pre_clear=True,
            post_pause=True,
            header="Row-Echelon Form: "
        )