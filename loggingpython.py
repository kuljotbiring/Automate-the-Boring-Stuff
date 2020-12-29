import logging

logging.basicConfig(level=logging.DEBUG, format='$asctime)s - %(levelname)s - %(message)s')

"""if you would rather have the logs go to a file, supply the file name"""
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='$asctime)s - %(levelname)s - %(message)s')


"""This next line will disable the logging statements from showing. uncomment to activate
    it says ignore everything rated as CRITICAL or below"""
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')


def factorial(num):
    logging.debug('Start of factorial(%s)' % (num))
    total = 1
    for i in range(1, num + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total


print(factorial(5))