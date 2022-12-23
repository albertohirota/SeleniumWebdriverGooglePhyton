import logging
logging.basicConfig(
    filename='C:\\temp\\Logs.log', 
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%Y/%m/%d %I:%M:%S %p',
    encoding='utf-8',
    level=logging.INFO)

Instance = None

