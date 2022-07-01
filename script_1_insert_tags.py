# Summary: Program to modify our kb articles for import into TDX 
# Details: 
# Last Modified: 20220629
# Modified by: JM

### import libraries

import os, re

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
	index_filename = 'indextest.txt'

	with open(os.path.join(path_of_the_directory,index_filename)) as index_file:
		for line in index_file:
			print(line.rstrip())
			# get filename part
			x = re.search(r"\d{8}-\d{2}", line)
			#print(x.group()) 
			match_part = x.group()
			# look for associated file
			for filename in os.listdir(path_of_the_directory):
				if filename.startswith(match_part):
					#print(filename)
					# insert line from index file into corresponding file
					with open(os.path.join(path_of_the_directory,filename), "r", encoding='utf8') as f:
						contents = f.readlines()

					contents.insert(1, '\n<p>Tags: '+line.rstrip()+'</p>\n')

					#with open(os.path.join(path_of_the_directory,'fixed-'+filename), "w", encoding='utf8') as f:
					with open(os.path.join(path_of_the_directory,filename), "w", encoding='utf8') as f:
						contents = "".join(contents)
						f.write(contents)




### run main function if this file is loaded as the main program 
if __name__ == "__main__":
	main()