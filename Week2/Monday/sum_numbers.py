import sys

def sum_numbers(file_name):
	file = open(file_name,"r")
	string = [] 
	string.append(file.read())
	string = str(string)
	string1 = string.split(" ")
	return string1

	

if __name__ == '__main__':
	print(sum_numbers(sys.argv[1]))