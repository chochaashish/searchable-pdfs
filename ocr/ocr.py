import os

def convert_image_to_searchable_pdf(file_name):
	os.system('tesseract tmp/temp.tiff "'+file_name+'" -l deu  pdf')

def get_filename_word():
	os.system('tesseract tmp/temp.tiff tmp/temp -l deu')
	with open('tmp/temp.txt', 'r') as f:
		return [line.rstrip(' ') for line in open('tmp/temp.txt')][0].split()[0].rstrip(' ')
		# return ' '.rstrip(' ')
