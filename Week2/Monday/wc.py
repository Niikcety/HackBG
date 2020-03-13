import sys
import fileinput

def count_chars(filename):
	file = open(filename,'r')
	string = ''.join(file.read())
	file.close()

	return len(string)

def count_words(filename):
	file = open(filename,'r')
	string = ''.join(file.read())
	file.close()
	string1 = string.split(' ')
	return len(string1)

def count_lines(filename):
	file = open(filename,'r')
	lines = file.readlines()

	return len(lines)

def counter(control, filename):
	#control = str(ctr)
	if control == 'chars':
		print('Chars')
		return count_chars(filename)
	if control == 'words':
		print('Words')
		return count_words(filename)
	if control == 'lines':
		print('Lines')
		return count_lines(filename)
	return 'Invalid input'
if __name__ == '__main__':
	print(counter(sys.argv[1],sys.argv[2]))