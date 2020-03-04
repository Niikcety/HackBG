import sys
import fileinput

def cat(argument):
	file = open(argument,"r")
	print(file.read())
	file.close()    


def main(arg):
    cat(arg)

if __name__ == '__main__':
    main(sys.argv[1])