import os
import time
import csv
from datetime import datetime

import config
from error import error_logs
LOGGER = error_logs.get_logger(__name__)

password_dict = config.PASSWORD_DICT
def convert_pdf_to_image(file_name):
	open_file = False
	try:
		e_1 = os.system('magick convert -density 300 "'+file_name+'" -depth 8 \
			-strip -background white -alpha off tmp/temp.tiff')
		if e_1 == 1:
			open_file = True
			raise Exception('Error')
	except Exception as e:
		password = password_dict.get(file_name)
		if password:
			e_2 = os.system('mogrify -authenticate '+password+' -density 300 '+file_name)
			if e_2 == 1:
				return False
			LOGGER.info('{} file: {} is opened with password {}'.format(datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), file_name, password))
		else:
			return False
	finally:
		if open_file:
			os.system('magick convert -density 300 "'+file_name+'" -depth 8 \
			-strip -background white -alpha off tmp/temp.tiff')
	return True

def check_file():
	filename = config.LOG_PDF_FILENAME
	rows = []
	# reading csv file
	with open(filename, 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			if row:
				rows.append(row[0])
	return rows
