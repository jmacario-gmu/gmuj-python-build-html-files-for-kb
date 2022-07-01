# Summary: Program to modify our kb articles for import into TDX 
# Details: 
# Last Modified: 20220629
# Modified by: JM

### import libraries

import os, re, unicodedata

### define functions

def slugify(value, allow_unicode=False):
	"""
	Taken from https://github.com/django/django/blob/master/django/utils/text.py
	Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
	dashes to single dashes. Remove characters that aren't alphanumerics,
	underscores, or hyphens. Convert to lowercase. Also strip leading and
	trailing whitespace, dashes, and underscores.
	"""
	value = str(value)
	if allow_unicode:
	    value = unicodedata.normalize('NFKC', value)
	else:
	    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
	value = re.sub(r'[^\w\s-]', '', value.lower())
	return re.sub(r'[-\s]+', '-', value).strip('-_')

### define main

def main():

	path_of_the_directory = 'C:/Users/jmacario/Documents/development/python/development/gmuj-python-build-html-files-for-kb'

	ext = ('.html')

	for filename in os.listdir(path_of_the_directory):
		if filename.endswith(ext):
			print(filename)

			f = open(os.path.join(path_of_the_directory,filename), encoding='utf8')
			
			for line in f:
				#print(line.rstrip())
				# get filename part
				x = re.search("<h2>([^<]*)", line)
				if x:
					#print(x.group()) 
					match_part = x.group(1)
					print(match_part)
					print(slugify(match_part))

			f.close()
			os.rename(filename, slugify(match_part)+'.html')

		else:
			continue

### run main function if this file is loaded as the main program 
if __name__ == "__main__":
	main()