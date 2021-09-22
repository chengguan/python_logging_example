
import logging
from my_module import *

module_logger = logging.getLogger('my_module').setLevel(level=logging.WARNING)

def main():
    logging.basicConfig(filename='myapp.log', 
                level=logging.INFO, 
                format='%(asctime)s [%(module)s:%(funcName)s] %(message)s')
    logger = logging.getLogger(__name__)

    fh = logging.FileHandler('root.log')
    fh.setLevel(logging.WARNING)

    root_logger = logging.getLogger()
    root_logger.addHandler(fh)

    foo()

    b = Bar()
    b.bar()
    logger.info('test.')
    root_logger.info('root')

if __name__ == '__main__':
    main()