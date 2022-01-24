# Import the required Modules
#import tabula
import os.path
import pdfplumber
#import pyPdf #returns an error "ModuleNotFoundError: No module named 'pdf' " https://www.quora.com/Which-Python-library-will-let-me-check-how-many-pages-are-in-a-PDF-file

#if there is a comma inside a description. Tableau understands it as a new column


#Global variables
File_name = 'CompleteListofRegistrations(from1948to2021)'
number_of_pages = 251
number_of_records = 0

#Test global vars
col_numbers = 0

#Get number of pages in the PDF file
PDF_file_name = File_name + '.pdf'
#reader = pyPdf.PdfFileReader(open(PDF_file_name))
#number_of_pages = reader.getNumPages() 
#print(number_of_pages)

#Check if the file for conversion exists
CSV_file_name = File_name + '.csv'

if os.path.exists(CSV_file_name) == False:
	with open(CSV_file_name, "a") as outfile:		
			outfile.write('Cultivar;Reg NO;Hybridizer;Year;Form;Growth;Corolla Color;Sepal Color;Tube Color;Parentage' + '\n')
		
	# Read a PDF File	
	PDF_file = pdfplumber.open(PDF_file_name)
	for p in range(0, number_of_pages):
		print('Current page in work: ', p)
		p0 = PDF_file.pages[p]
		table = p0.extract_table()
		
		for i in range(0, len(table)):
			with open(CSV_file_name, "a") as outfile:
				try:
					for ltr in range(0, 10):
						#for ch in range(0, len(table[i][ltr])):
							#if table[i][ltr][ch] == '\n':
								#print('in the small cycle', table[i][ltr])
							#	table[i][ltr][ch] = table[i][ltr][ch].replace('\n', ' ')
						element_to_write = str(table[i][ltr].replace('\n', ' '))
						outfile.write(element_to_write + ';')
					outfile.write('\n')
						
				except:
					print(table[i])
					continue

	
else: print('File is already converted from PDF')


