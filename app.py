
import logging
from my_module import *

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO, 
                format='%(asctime)s [%(module)s:%(funcName)s] %(message)s', 
                datefmt='%m/%d/%Y %H:%M:%S')

    # import logging.config
    # logging.config.fileConfig('logging.conf')
    # your program code

    foo()

    b=Bar()
    b.bar()
    logging.info('test.')

if __name__ == '__main__':
    main()