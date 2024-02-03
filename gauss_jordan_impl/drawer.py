import os

def clear():
    if os.name == 'posix':
        os.system("clear")
    else:
        os.system("cls")

def pause():
    input('\nPress enter to continue...')

def draw_matrix(
    matrix: list[list[int | float]],
    m: int, n: int,
    cell_len: int,
    *,
    pre_clear: bool = False,
    post_pause: bool = False,
    header: str = '',
) -> None:

    border_vertical = "│"
    border_topleft = "┌"
    border_topright = "┐"
    border_bottomleft = "└"
    border_bottomright = "┘"
    delimiter = ' • '
    here = '◆'

    # Clearing screen
    if pre_clear:
        clear()

    view = f"\n{header}"
    empty_cell = f'{" " * cell_len}'
    current_cell = f'{here:^{cell_len}}'

    for i in range(m):

        # Setting borders
        if i == 0:
            prefix = border_topleft
            sufix = border_topright
        elif i + 1 == m:
            prefix = border_bottomleft
            sufix = border_bottomright
        else:
            sufix = prefix = border_vertical

        cells = []

        if i >= len(matrix):
            cells = [empty_cell] * n
        else:
            for j in range(n):
                if j < len(matrix[i]):
                    cells.append(f'{matrix[i][j]:^{cell_len}}')
                    continue
                cells.append(current_cell)
                cells.extend([empty_cell] * (n - j - 1))
                break

        cells_str = delimiter.join(cells)
        row = f'{prefix} {cells_str} {sufix}'
        view = f'{view}\n{row}'

    print(view)
    if post_pause:
        pause()
