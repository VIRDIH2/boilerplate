import utils.log
import logging.config

def initialize(): 
    utils.log.init()

def main():
    initialize()

    logger = logging.getLogger("MAIN")
    logger.warning('Watch out!')  # will print a message to the console
    logger.info('I told you so')  # will  print 
    logger.debug('Hmmm...') # will not print anything

    print("Hello World")

if __name__== '__main__':
    main()

