# Summary: Program to modify our kb articles for import into TDX 
# Details: 
# Last Modified: 20220629
# Modified by: JM

### import libraries

import os

### define functions

def fnOutputStringToFile(inputString,outputFileName):
	##
	# Summary: outputs a string to a file
	# Details: string to output and the name of the file to output to are specified as parameters
	# Last Modified: 20161004
	# Modified by: JM
	##

	# this script had been using: open(outputFileName, "w"), but some pages had characters that failed unless in binary mode
	# therefore I am now doing: open(outputFileName, "wb"), 
	# this then requires that the string be encoded as binary, hence the: text_file.write(inputString.encode('utf-8'))
	# prior to switching the file open mode to binary, this encoding was not needed

	# open/create text file for output ("wb" indicates opening file for writing binary data)
	text_file = open(outputFileName, "wb")
	# write output string to file
	text_file.write(inputString.encode('utf-8'))
	# close text file
	text_file.close()

### define main

def main():

	path_of_the_directory = 'C:/Users/jmacario/Documents/development/python/development/gmuj-python-build-html-files-for-kb'

	# Read template top file to variable
	f = open(os.path.join(path_of_the_directory,"html-template-top.txt"))
	html_template_top_content = f.read()
	f.close()
	#print(html_template_top_content)

	# Read template bottom file to variable
	f = open(os.path.join(path_of_the_directory,"html-template-bottom.txt"))
	html_template_bottom_content = f.read()
	f.close()
	#print(html_template_bottom_content)

	ext = ('.html')
	for filename in os.listdir(path_of_the_directory):
		if filename.endswith(ext):
			print(filename)
			f = open(os.path.join(path_of_the_directory,filename), encoding='utf8')
			html_file_content = f.read()
			f.close()
			fixed_file = html_template_top_content + html_file_content + html_template_bottom_content
			print(fixed_file)
			#fnOutputStringToFile(fixed_file,'fixed_'+filename)
			fnOutputStringToFile(fixed_file,filename)
		else:
			continue

### run main function if this file is loaded as the main program 
if __name__ == "__main__":
	main()