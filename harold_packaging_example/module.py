import sys

import harold_packaging_example.util.utils as utils


def main():
    for arg in sys.argv[1:]:
        print(utils.translate(arg))
    
    
if __name__ == '__main__':
    main()
    