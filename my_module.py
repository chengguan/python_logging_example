#my_module
import logging

logger = logging.getLogger(__name__)

def foo():
    logger.info('Hi, foo, info.')
    logger.warning('Hi, foo, warning.')

class Bar(object):
    def bar(self):
        root_logger = logging.getLogger()
        root_logger.error('error')
        logger.info('Hi, bar')