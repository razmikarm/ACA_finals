import os
import numpy as np
from matrices import Matrix, CoefficientMatrix, ConstantMatrix


class Helper:

    @staticmethod
    def get_int(msg, safe: bool) -> int:
        num_str = input(msg)
        if not safe:
            return int(num_str)
        while not num_str.isdigit() and num_str != '0':
            num_str = input(msg)
            print("Invalid data. Try again!")
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
        Helper.clear()
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
                Helper.draw_matrix(matrix_list, m, n, cell_len, True)
                msg = f'Enter value for [{i}, {j}] position: '
                num = Helper.get_number(msg, safe=True)
                if len(str(num)) > cell_len:
                    cell_len = len(str(num))
                matrix_list[-1].append(num)
        return CoefficientMatrix(matrix_list)

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
            Helper.draw_matrix(vector_list, m, 0, cell_len, True)
            msg = f'Enter {i}{pos} value: '
            num = Helper.get_number(msg, safe=True)
            if len(str(num)) > cell_len:
                cell_len = len(str(num))
            vector_list.append(num)
        return ConstantMatrix(vector_list)

    @staticmethod
    def pause():
        input('\nPress enter to continue...')

    @staticmethod
    def clear():
        if os.name == 'posix':
            os.system("clear")
        else:
            os.system("cls")

    @staticmethod
    def draw_matrix(
        matrix: list[list[int | float]],
        m: int,
        n: int = 0,
        cell_len: int = None,
        clear: bool = False,
        *,
        header: str = '',
    ) -> None:

        # Clearing screen
        if clear:
            Helper.clear()



        border_vertical = "│"
        border_topleft = "┌"
        border_topright = "┐"
        border_bottomleft = "└"
        border_bottomright = "┘"
        here = '◆'

        if cell_len is None:
            maxx = 1
            k = lambda x: len(str(x))
            for row in matrix:
                if isinstance(row, list) and row:
                    maxx = max(maxx, max(row, key=k), key=k)
                elif isinstance(row, (int, float)):
                    maxx = max(maxx, row, key=k)
            cell_len = len(str(maxx))


        view = f"\n{header}"
        for i in range(m):
            if i == 0:
                prefix = border_topleft
                sufix = border_topright
            elif i + 1 == m:
                prefix = border_bottomleft
                sufix = border_bottomright
            else:
                sufix = prefix = border_vertical

            cells = ''
            
            # if drawing vector
            if n == 0:
                if i < len(matrix):
                    cells = f'{matrix[i]:^{cell_len}}'
                elif i == len(matrix):
                    cells = f'{here:^{cell_len}}'
                else:
                    cells = f'{" " * cell_len}'

            for j in range(n):
                if i < len(matrix):
                    if j < len(matrix[i]):
                        cell = f'{matrix[i][j]:^{cell_len}}'
                    elif j == len(matrix[i]):
                        cell = f'{here:^{cell_len}}'
                    else:
                        cell = f'{" " * cell_len}'
                else:
                    cell = f'{" " * cell_len}'

                if cells == '':
                    cells = cell
                else:
                    cells = f"{cells} • {cell}"

            row = f'{prefix} {cells} {sufix}'
            view = f'{view}\n{row}'
        print(view)
