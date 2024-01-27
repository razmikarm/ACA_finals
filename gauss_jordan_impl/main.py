from impl import SLE
from helper import Helper

def main():
    m, n = Helper.get_dimensions()
    coefficient = Helper.get_coeficent_matrix(m, n)
    constant = Helper.get_constant_matrix(m)
    Helper.clear()
    Helper.draw_matrix(constant, m, header='Constant Matrix:')
    Helper.draw_matrix(coefficient, m, n, header='Coefficient Matrix:')
    Helper.confirm()
    sle = SLE(coefficient, constant)
    sle.to_ref()

if __name__ == '__main__':
    main()
