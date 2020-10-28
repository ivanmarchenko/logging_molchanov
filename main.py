import logging

# logger = logging.getLogger()
# print(logger)

logging.basicConfig() 
app_logger = logging.getLogger('app_logger')

console_handler = logging.StreamHandler()
app_logger.addHandler(console_handler )

f = logging.Formatter(fmt='%(levelname)s - %(name)s - %(message)s')
console_handler.setFormatter(f)

utils_logger = logging.getLogger('app_logger.utils')
utils_logger.setLevel('DEBUG')



def main():
    utils_logger.debug('Hello')  

if __name__ == "__main__": 
    main()