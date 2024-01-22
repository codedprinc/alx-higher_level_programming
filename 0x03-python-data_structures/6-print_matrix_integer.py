#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        if matrix:
            for elems in matrix:
                i = 1
                leng = len(elems)

                for elem in elems:
                    if i == leng:
                        print('{:d}'.format(elem), end='')
                    else:
                        print('{:d}'.format(elem), end=' ')
                    i += 1

                print()
