from tests import append_numbers, gen_random_numbers, square_numbers
import argparse
import numpy as np
import scipy as sp

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("dims", help="Number of dimensions to test",
                    type=int)
    args = parser.parse_args()
    N = args.dims
    print(f'Test append_numbers with {N}.')
    append_numbers(N)

    print(f'Test gen_random_numbers with {N}.')
    gen_random_numbers(N)

    print(f'Test square_numbers with {N}.')
    square_numbers(N)

    np.core.test()

    sp.test()


