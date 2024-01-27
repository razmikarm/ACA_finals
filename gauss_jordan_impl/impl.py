import numpy as np


class SLE:
    
    def __init__(self, coef, const):
        self.coef = coef
        self.const = const
        # elementary row operations
        self.elops = {
            "Interchange two rows | (Ri ↔ Rj)": None,
            "Multiply a row by a non-zero constant | (c · Rj)": None,
            "Add a multiple of a row to another row | (Ri + c · Rj)": None,
        }

    # Transform to row-echelon form
    def to_ref(self):
        """
        Step 1. If the matrix consists entirely of zeros, stop.
        Step 2. Otherwise, find the row that contains the leftmost nonzero
                entry of the matrix (call that entry a).
        Step 3. Move that row to the top position.
        Step 4. Multiply that row by 1/a to create a leading 1.
        Step 5. By subtracting multiples of that row from rows below it,
                make the entries below the leading 1 in that column all 0.
        Step 6. Fix the first row, and repeat steps 1-5 on the matrix
                consisting of the remaining rows (we don't touch the first
                row anymore).
        """
        pass
