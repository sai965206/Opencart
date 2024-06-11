import logging

path = 'D:\\OpenCartProject1\\logs\\automation.log'
def Log():
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)
	file = logging.FileHandler(path)
	format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y:%m:%d %I:%M:%S %p')
	file.setFormatter(format)
	logger.addHandler(file)
	return logger