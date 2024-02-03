from sle import SLE
from helper import Helper

def main():
    m, n = Helper.get_dimensions()
    coefficient = Helper.get_coeficent_matrix(m, n)
    constant = Helper.get_constant_matrix(m)
    sle = SLE(coefficient, constant)
    coefficient.draw(pre_clear=True)
    constant.draw()
    sle.aug.draw(post_pause=True)
    sle.to_ref()

if __name__ == '__main__':
    main()
