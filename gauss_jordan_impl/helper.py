import numpy as np
from drawer import clear, draw_matrix
from matrices import Matrix, CoefficientMatrix, ConstantMatrix


class Helper:

    @staticmethod
    def get_int(msg, safe: bool) -> int:
        num_str = input(msg)
        if not safe:
            return int(num_str)
        while not num_str.isdigit() and num_str != '0':
            print("Invalid data. Try again!")
            num_str = input(msg)
        return int(num_str)

    @staticmethod
    def get_float(msg, safe: bool) -> float:
        num_str = input(msg)
        if not safe:
            return float(num_str)
        num = 0
        while True:
            try:
                return float(num_str)
            except:
                print("Invalid data. Try again!")
                num_str = input(msg)
    
    @staticmethod
    def get_number(msg, safe: bool) -> int | float:
        number = Helper.get_float(msg, safe)
        if number.is_integer():
            number = int(number)
        return number

    @staticmethod
    def get_dimensions():
        clear()
        m = Helper.get_int('Enter row count: ', safe=True)
        n = Helper.get_int('Enter column count: ', safe=True)
        return m, n

    @staticmethod
    def get_coeficent_matrix(m: int, n: int) -> CoefficientMatrix:
        matrix_list = []
        cell_len = 1
        for i in range(1, m+1):
            matrix_list.append([])
            for j in range(1, n+1):
                draw_matrix(matrix_list, m, n, cell_len, pre_clear=True)
                msg = f'Enter value for [{i}, {j}] position: '
                num = Helper.get_number(msg, safe=True)
                if len(str(num)) > cell_len:
                    cell_len = len(str(num))
                matrix_list[-1].append(num)
        return CoefficientMatrix(matrix_list, cell_len)

    @staticmethod    
    def get_constant_matrix(m: int) -> ConstantMatrix:
        vector_list = []
        poses = {
            1: 'st',
            2: 'nd',
            3: 'rd',
        }
        cell_len = 1
        for i in range(1, m+1):
            pos = poses.get(i, 'th')
            draw_matrix(vector_list, m, 1, cell_len, pre_clear=True)
            msg = f'Enter {i}{pos} value: '
            num = Helper.get_number(msg, safe=True)
            if len(str(num)) > cell_len:
                cell_len = len(str(num))
            vector_list.append([num])
        return ConstantMatrix(vector_list, cell_len)
