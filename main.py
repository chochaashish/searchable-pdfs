# magick -density 300 -compress lzw -units 2 "30.pdf" -resize 100% "MED.PNG"

# tesseract MED2.PNG out2 -l deu pdf
import os
import time
import csv
from datetime import datetime

import config
from error import error_logs
from ocr.password_data import load_password
from ocr.data import convert_pdf_to_image, check_file
from ocr.ocr import convert_image_to_searchable_pdf, get_filename_word
SEARCHABLE_FOLDER = config.SEARCHABLE_FOLDER
ROOT_FOLDER = config.ROOT_FOLDER

LOGGER = error_logs.get_logger(__name__)
def main():
	"""Main Script"""
	input_path_list = []
	checked_pdf_list = check_file()
	for path, subdirs, files in os.walk(ROOT_FOLDER):
		for name in files:
			input_path = os.path.join(path, name)
			if name.endswith('.pdf') :
				if input_path not in checked_pdf_list:

					if convert_pdf_to_image(input_path):
						if get_filename_word():
							name = get_filename_word()
						os.remove(input_path)
						output_path = os.path.join(path, name).replace('.pdf', '')
						input_path_list.append(os.path.join(path, name))
						convert_image_to_searchable_pdf(output_path)
					else:
						LOGGER.info('{} file: {} is password protected, and password is not available or wrong for this file'.format(datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), input_path))
					LOGGER.info('{} processed file: {}'.format(datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), input_path))
				else:
					LOGGER.info('{} already processed file: {}'.format(datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), input_path))

	with open(config.LOG_PDF_FILENAME, "a+") as f:
		writer = csv.writer(f)
		for row in input_path_list :
			if row not in checked_pdf_list:
				writer.writerows([[row]])

if __name__ == '__main__':
	load_password()
	main()
