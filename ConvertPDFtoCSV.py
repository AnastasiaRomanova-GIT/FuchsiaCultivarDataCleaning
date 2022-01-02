# Import the required Modules
import tabula
import os.path

#Global variables
File_name = 'CompleteListofRegistrations(from1948to2021)'
number_of_records = 0

#Test global vars
col_numbers = 0

#Check if the file for conversion exists
CSV_file_name = File_name + '.csv'
if os.path.exists(CSV_file_name) == False:
	# Read a PDF File
	PDF_file_name = File_name + '.pdf'
	df = tabula.read_pdf(PDF_file_name, pages='all')[0]
	# convert PDF into CSV	
	tabula.convert_into(PDF_file_name, CSV_file_name, output_format="csv", pages='all', lattice=True)
	print(df)
else: print('File is already converted from PDF')

#remove empty cells in the beginning of some lines
Read_file_handle = open(CSV_file_name, 'r')
Corrected_file_name = File_name + '_Corrected.csv'
Write_file_handle = open(Corrected_file_name, 'w')
for line in Read_file_handle:
	number_of_records += 1
	words = line.split(',')
	#print(words[0])

	if len(words) != 10:
		col_numbers += 1
		continue

	if words[0] == '""': 
		#print('Irregularity is found')
		words.remove(words[0])
		for element in words:
			Write_file_handle.write(element)
		#Write_file_handle.write('\n')
	else: 
		for element in words:
			Write_file_handle.write(element + ',')
		#Write_file_handle.write('\n')
Write_file_handle.close()
Read_file_handle.close()
print('Cleaning is done')

print('Columns with non-standard length: ', col_numbers)
print('Number of records: ', number_of_records)

